"""
ONI Framework Data Export

Exports NeuroSim data in formats compatible with the
ONI (Organic Neural Interface) Framework.

Maps simulation data to the 14-layer neural model and
computes coherence metrics.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Tuple
from enum import Enum
import numpy as np
import json
from datetime import datetime


# ONI Framework 14-layer model
ONI_LAYER_NAMES = {
    1: "Physical Interface",
    2: "Signal Transduction",
    3: "Pattern Recognition",
    4: "Feature Integration",
    5: "Temporal Processing",
    6: "Memory Encoding",
    7: "Contextual Association",
    8: "Decision Making",
    9: "Motor Planning",
    10: "Action Selection",
    11: "Feedback Integration",
    12: "Error Correction",
    13: "Learning/Adaptation",
    14: "Meta-Cognition",
}


class ONIDataFormat(Enum):
    """Output formats for ONI data."""
    JSON = "json"
    NUMPY = "numpy"
    ONI_NATIVE = "oni"  # Format compatible with oni-framework package


@dataclass
class LayerMetrics:
    """Metrics for a single ONI layer."""
    layer_id: int
    name: str
    n_neurons: int = 0
    n_spikes: int = 0
    mean_rate: float = 0.0          # Hz
    mean_voltage: float = 0.0        # mV
    synchrony: float = 0.0           # 0-1
    coherence: float = 0.0           # Cs metric


@dataclass
class ONIExportData:
    """Data structure for ONI export."""

    # Metadata
    timestamp: str = ""
    duration: float = 0.0
    dt: float = 0.1
    n_total_neurons: int = 0
    n_total_spikes: int = 0

    # Layer data
    layers: Dict[int, LayerMetrics] = field(default_factory=dict)

    # Inter-layer connectivity
    connectivity_matrix: np.ndarray = None

    # Global metrics
    global_coherence: float = 0.0
    mean_firing_rate: float = 0.0
    network_synchrony: float = 0.0

    # Time series (downsampled)
    time_vector: np.ndarray = None
    layer_activities: Dict[int, np.ndarray] = None

    # Spike data
    spike_trains: Dict[int, Dict[str, List[float]]] = None


class ONIExporter:
    """
    Exports NeuroSim data to ONI Framework format.

    Maps simulation results to the 14-layer neural model
    and computes relevant metrics for neural security analysis.

    Usage:
        >>> from neurosim.export import ONIExporter

        >>> # After running simulation
        >>> exporter = ONIExporter()
        >>> oni_data = exporter.export(result, network)
        >>> exporter.save(oni_data, "simulation_oni.json")
    """

    def __init__(
        self,
        downsample_factor: int = 10,
        compute_coherence: bool = True
    ):
        """
        Initialize exporter.

        Args:
            downsample_factor: Factor to downsample time series
            compute_coherence: Whether to compute coherence metrics
        """
        self.downsample_factor = downsample_factor
        self.compute_coherence = compute_coherence

    def export(
        self,
        result,  # SimulationResult
        network,  # Network
    ) -> ONIExportData:
        """
        Export simulation data to ONI format.

        Args:
            result: SimulationResult from engine
            network: Network that was simulated

        Returns:
            ONIExportData structure
        """
        data = ONIExportData(
            timestamp=datetime.now().isoformat(),
            duration=result.duration,
            dt=result.dt,
            n_total_neurons=result.n_neurons,
            n_total_spikes=result.total_spikes,
        )

        # Map neurons to ONI layers
        layer_neurons = self._map_neurons_to_layers(network)

        # Compute per-layer metrics
        for layer_id in range(1, 15):
            metrics = self._compute_layer_metrics(
                layer_id,
                layer_neurons.get(layer_id, []),
                result,
                network
            )
            data.layers[layer_id] = metrics

        # Compute connectivity matrix
        data.connectivity_matrix = self._compute_connectivity(network, layer_neurons)

        # Compute global metrics
        data.global_coherence = self._compute_global_coherence(data.layers)
        data.mean_firing_rate = result.mean_firing_rate
        data.network_synchrony = self._compute_synchrony(result, network)

        # Extract time series
        if result.t is not None and len(result.t) > 0:
            data.time_vector = result.t[::self.downsample_factor]
            data.layer_activities = self._compute_layer_activities(
                result, layer_neurons
            )

        # Extract spike trains by layer
        data.spike_trains = self._extract_spike_trains(result, layer_neurons)

        return data

    def _map_neurons_to_layers(self, network) -> Dict[int, List[str]]:
        """Map neurons to ONI layers based on their oni_layer attribute."""
        layer_neurons = {i: [] for i in range(1, 15)}

        for neuron_id, neuron in network.neurons.items():
            layer = getattr(neuron.params, 'oni_layer', None)

            if layer and 1 <= layer <= 14:
                layer_neurons[layer].append(neuron_id)
            else:
                # Default mapping based on position or group
                # If no layer specified, distribute evenly
                if hasattr(network, '_layer_neurons'):
                    # For LayeredNetwork, use layer structure
                    for layer_idx, neuron_ids in network._layer_neurons.items():
                        if neuron_id in neuron_ids:
                            # Map network layers to 14 ONI layers
                            oni_layer = int((layer_idx / len(network._layer_neurons)) * 13) + 1
                            layer_neurons[oni_layer].append(neuron_id)
                            break

        return layer_neurons

    def _compute_layer_metrics(
        self,
        layer_id: int,
        neuron_ids: List[str],
        result,
        network
    ) -> LayerMetrics:
        """Compute metrics for a single layer."""
        metrics = LayerMetrics(
            layer_id=layer_id,
            name=ONI_LAYER_NAMES.get(layer_id, f"Layer {layer_id}"),
            n_neurons=len(neuron_ids),
        )

        if not neuron_ids:
            return metrics

        # Count spikes
        total_spikes = 0
        for nid in neuron_ids:
            if result.spike_counts and nid in result.spike_counts:
                total_spikes += result.spike_counts[nid]

        metrics.n_spikes = total_spikes

        # Compute firing rate
        duration_sec = result.duration / 1000
        if duration_sec > 0 and len(neuron_ids) > 0:
            metrics.mean_rate = total_spikes / len(neuron_ids) / duration_sec

        # Compute mean voltage
        if result.voltages:
            voltages = []
            for nid in neuron_ids:
                if nid in result.voltages:
                    voltages.extend(result.voltages[nid])
            if voltages:
                metrics.mean_voltage = np.mean(voltages)

        # Compute synchrony within layer
        if result.spike_times and self.compute_coherence:
            metrics.synchrony = self._compute_layer_synchrony(
                neuron_ids, result.spike_times
            )

        # Compute coherence (simplified Cs metric)
        if self.compute_coherence:
            metrics.coherence = self._compute_layer_coherence(
                metrics.mean_rate,
                metrics.synchrony,
                len(neuron_ids)
            )

        return metrics

    def _compute_layer_synchrony(
        self,
        neuron_ids: List[str],
        spike_times: Dict[str, List[float]]
    ) -> float:
        """
        Compute spike synchrony within a layer.

        Uses a simple coincidence measure: fraction of spikes
        that occur within a small window of each other.
        """
        if len(neuron_ids) < 2:
            return 0.0

        all_spikes = []
        for nid in neuron_ids:
            if nid in spike_times:
                for t in spike_times[nid]:
                    all_spikes.append((t, nid))

        if len(all_spikes) < 2:
            return 0.0

        # Sort by time
        all_spikes.sort(key=lambda x: x[0])

        # Count coincidences (spikes within 5ms window from different neurons)
        window = 5.0  # ms
        coincidences = 0
        total_pairs = 0

        for i, (t1, n1) in enumerate(all_spikes):
            for j in range(i + 1, len(all_spikes)):
                t2, n2 = all_spikes[j]
                if t2 - t1 > window:
                    break
                if n1 != n2:
                    coincidences += 1
                    total_pairs += 1

        if total_pairs == 0:
            return 0.0

        return coincidences / total_pairs

    def _compute_layer_coherence(
        self,
        rate: float,
        synchrony: float,
        n_neurons: int
    ) -> float:
        """
        Compute coherence metric (simplified Cs).

        Based on ONI Framework's coherence calculation:
        Cs = f(rate, synchrony, connectivity)
        """
        if n_neurons == 0:
            return 0.0

        # Normalize rate (typical cortical rates 1-50 Hz)
        rate_norm = min(rate / 50.0, 1.0)

        # Coherence combines rate and synchrony
        # Higher is more coherent
        coherence = (rate_norm * 0.4 + synchrony * 0.6)

        return coherence

    def _compute_global_coherence(
        self,
        layers: Dict[int, LayerMetrics]
    ) -> float:
        """Compute global coherence across all layers."""
        coherences = [l.coherence for l in layers.values() if l.n_neurons > 0]
        if not coherences:
            return 0.0
        return np.mean(coherences)

    def _compute_synchrony(self, result, network) -> float:
        """Compute global network synchrony."""
        if not result.spike_times:
            return 0.0

        all_neuron_ids = list(network.neurons.keys())
        return self._compute_layer_synchrony(all_neuron_ids, result.spike_times)

    def _compute_connectivity(
        self,
        network,
        layer_neurons: Dict[int, List[str]]
    ) -> np.ndarray:
        """Compute inter-layer connectivity matrix."""
        conn = np.zeros((14, 14))

        # Get neuron to layer mapping
        neuron_to_layer = {}
        for layer_id, neuron_ids in layer_neurons.items():
            for nid in neuron_ids:
                neuron_to_layer[nid] = layer_id

        # Count connections between layers
        for synapse in network.synapses:
            pre_layer = neuron_to_layer.get(synapse.pre.id)
            post_layer = neuron_to_layer.get(synapse.post.id)

            if pre_layer and post_layer:
                conn[pre_layer - 1, post_layer - 1] += synapse.weight

        return conn

    def _compute_layer_activities(
        self,
        result,
        layer_neurons: Dict[int, List[str]]
    ) -> Dict[int, np.ndarray]:
        """Compute time-resolved activity for each layer."""
        activities = {}

        if result.t is None or len(result.t) == 0:
            return activities

        t_down = result.t[::self.downsample_factor]
        n_samples = len(t_down)

        for layer_id, neuron_ids in layer_neurons.items():
            if not neuron_ids:
                activities[layer_id] = np.zeros(n_samples)
                continue

            # Compute mean voltage trace
            layer_v = []
            for nid in neuron_ids:
                if result.voltages and nid in result.voltages:
                    v = result.voltages[nid][::self.downsample_factor]
                    if len(v) == n_samples:
                        layer_v.append(v)

            if layer_v:
                activities[layer_id] = np.mean(layer_v, axis=0)
            else:
                activities[layer_id] = np.zeros(n_samples)

        return activities

    def _extract_spike_trains(
        self,
        result,
        layer_neurons: Dict[int, List[str]]
    ) -> Dict[int, Dict[str, List[float]]]:
        """Extract spike trains organized by layer."""
        spike_trains = {}

        for layer_id, neuron_ids in layer_neurons.items():
            spike_trains[layer_id] = {}
            for nid in neuron_ids:
                if result.spike_times and nid in result.spike_times:
                    spike_trains[layer_id][nid] = list(result.spike_times[nid])

        return spike_trains

    def save(
        self,
        data: ONIExportData,
        filename: str,
        format: ONIDataFormat = ONIDataFormat.JSON
    ):
        """
        Save ONI export data to file.

        Args:
            data: ONIExportData to save
            filename: Output filename
            format: Output format
        """
        if format == ONIDataFormat.JSON:
            self._save_json(data, filename)
        elif format == ONIDataFormat.NUMPY:
            self._save_numpy(data, filename)
        elif format == ONIDataFormat.ONI_NATIVE:
            self._save_oni_native(data, filename)

    def _save_json(self, data: ONIExportData, filename: str):
        """Save as JSON."""
        output = {
            "metadata": {
                "timestamp": data.timestamp,
                "duration_ms": data.duration,
                "dt_ms": data.dt,
                "n_neurons": data.n_total_neurons,
                "n_spikes": data.n_total_spikes,
                "format": "oni_neurosim_v1",
            },
            "global_metrics": {
                "coherence": data.global_coherence,
                "mean_firing_rate_hz": data.mean_firing_rate,
                "synchrony": data.network_synchrony,
            },
            "layers": {},
        }

        # Add layer data
        for layer_id, metrics in data.layers.items():
            output["layers"][str(layer_id)] = {
                "name": metrics.name,
                "n_neurons": metrics.n_neurons,
                "n_spikes": metrics.n_spikes,
                "mean_rate_hz": metrics.mean_rate,
                "mean_voltage_mv": metrics.mean_voltage,
                "synchrony": metrics.synchrony,
                "coherence": metrics.coherence,
            }

        # Add connectivity matrix
        if data.connectivity_matrix is not None:
            output["connectivity"] = data.connectivity_matrix.tolist()

        # Save
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)

    def _save_numpy(self, data: ONIExportData, filename: str):
        """Save as numpy archive."""
        save_dict = {
            "duration": data.duration,
            "dt": data.dt,
            "global_coherence": data.global_coherence,
            "mean_firing_rate": data.mean_firing_rate,
            "network_synchrony": data.network_synchrony,
        }

        if data.connectivity_matrix is not None:
            save_dict["connectivity"] = data.connectivity_matrix

        if data.time_vector is not None:
            save_dict["time"] = data.time_vector

        if data.layer_activities:
            for layer_id, activity in data.layer_activities.items():
                save_dict[f"layer_{layer_id}_activity"] = activity

        np.savez(filename, **save_dict)

    def _save_oni_native(self, data: ONIExportData, filename: str):
        """
        Save in ONI Framework native format.

        Compatible with the oni-framework Python package.
        """
        # Format compatible with oni-framework
        output = {
            "version": "1.0",
            "type": "neurosim_export",
            "timestamp": data.timestamp,
            "simulation": {
                "duration_ms": data.duration,
                "dt_ms": data.dt,
                "n_neurons": data.n_total_neurons,
            },
            "coherence_analysis": {
                "Cs_global": data.global_coherence,
                "layer_coherences": {
                    str(lid): lm.coherence
                    for lid, lm in data.layers.items()
                },
                "layer_synchrony": {
                    str(lid): lm.synchrony
                    for lid, lm in data.layers.items()
                },
            },
            "firing_statistics": {
                "total_spikes": data.n_total_spikes,
                "mean_rate_hz": data.mean_firing_rate,
                "layer_rates": {
                    str(lid): lm.mean_rate
                    for lid, lm in data.layers.items()
                },
            },
            "connectivity": {
                "inter_layer_weights": data.connectivity_matrix.tolist()
                if data.connectivity_matrix is not None else None,
            },
        }

        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)


def export_for_oni_attack_simulator(
    result,
    network,
    output_path: str
) -> str:
    """
    Export simulation data for use with ONI Attack Simulator.

    Args:
        result: SimulationResult
        network: Simulated network
        output_path: Output file path

    Returns:
        Path to exported file
    """
    exporter = ONIExporter()
    data = exporter.export(result, network)
    exporter.save(data, output_path, ONIDataFormat.ONI_NATIVE)
    return output_path
