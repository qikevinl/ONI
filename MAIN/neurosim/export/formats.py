"""
General Data Export Formats

Provides functions to export simulation data to various
standard formats for analysis and visualization.
"""

from typing import Dict, Any, List, Optional, Union
import numpy as np
import json


def export_to_numpy(
    result,
    filename: str,
    include_voltages: bool = True,
    include_spikes: bool = True
):
    """
    Export simulation results to numpy archive (.npz).

    Args:
        result: SimulationResult from simulation
        filename: Output filename (without .npz extension)
        include_voltages: Include voltage traces
        include_spikes: Include spike times
    """
    save_dict = {
        "duration": result.duration,
        "dt": result.dt,
        "n_steps": result.n_steps,
        "n_neurons": result.n_neurons,
        "n_synapses": result.n_synapses,
        "total_spikes": result.total_spikes,
        "mean_firing_rate": result.mean_firing_rate,
    }

    # Time vector
    if result.t is not None:
        save_dict["t"] = result.t

    # Voltage traces
    if include_voltages and result.voltages:
        neuron_ids = list(result.voltages.keys())
        save_dict["neuron_ids"] = np.array(neuron_ids, dtype=object)

        for nid, v in result.voltages.items():
            save_dict[f"V_{nid}"] = np.array(v)

    # Spike times
    if include_spikes and result.spike_times:
        for nid, times in result.spike_times.items():
            save_dict[f"spikes_{nid}"] = np.array(times)

    np.savez(f"{filename}.npz", **save_dict)


def export_to_json(
    result,
    filename: str,
    include_voltages: bool = False,  # Large, usually skip
    include_spikes: bool = True,
    indent: int = 2
):
    """
    Export simulation results to JSON.

    Args:
        result: SimulationResult from simulation
        filename: Output filename (without .json extension)
        include_voltages: Include voltage traces (warning: large)
        include_spikes: Include spike times
        indent: JSON indentation
    """
    output = {
        "metadata": {
            "duration_ms": result.duration,
            "dt_ms": result.dt,
            "n_steps": result.n_steps,
            "n_neurons": result.n_neurons,
            "n_synapses": result.n_synapses,
            "wall_time_sec": result.wall_time,
        },
        "summary": {
            "total_spikes": result.total_spikes,
            "mean_firing_rate_hz": result.mean_firing_rate,
        },
        "spike_counts": result.spike_counts or {},
    }

    if include_voltages and result.voltages:
        output["voltages"] = {
            nid: list(v) for nid, v in result.voltages.items()
        }

    if include_spikes and result.spike_times:
        output["spike_times"] = {
            nid: list(times) for nid, times in result.spike_times.items()
        }

    if result.t is not None:
        output["time_vector"] = list(result.t)

    with open(f"{filename}.json", 'w') as f:
        json.dump(output, f, indent=indent)


def export_to_csv(
    result,
    filename: str,
    variables: List[str] = None
):
    """
    Export voltage traces to CSV.

    Args:
        result: SimulationResult from simulation
        filename: Output filename (without .csv extension)
        variables: List of neuron IDs to include (None = all)
    """
    if not result.voltages or result.t is None:
        raise ValueError("No voltage data to export")

    # Determine which neurons to export
    if variables is None:
        neuron_ids = list(result.voltages.keys())
    else:
        neuron_ids = [nid for nid in variables if nid in result.voltages]

    if not neuron_ids:
        raise ValueError("No matching neuron IDs found")

    # Create data matrix
    n_samples = len(result.t)
    data = np.zeros((n_samples, len(neuron_ids) + 1))
    data[:, 0] = result.t

    for i, nid in enumerate(neuron_ids):
        v = result.voltages[nid]
        data[:, i + 1] = v[:n_samples]

    # Create header
    header = "time_ms," + ",".join(neuron_ids)

    # Save
    np.savetxt(
        f"{filename}.csv",
        data,
        delimiter=",",
        header=header,
        comments=""
    )


def export_spike_trains(
    result,
    filename: str,
    format: str = "csv"
):
    """
    Export spike trains to file.

    Formats:
    - csv: One row per spike (time, neuron_id)
    - json: Dictionary of neuron_id -> spike times
    - sparse: Sparse matrix format (time bin, neuron index)

    Args:
        result: SimulationResult from simulation
        filename: Output filename
        format: Output format (csv, json, sparse)
    """
    if not result.spike_times:
        raise ValueError("No spike data to export")

    if format == "csv":
        _export_spikes_csv(result.spike_times, filename)
    elif format == "json":
        _export_spikes_json(result.spike_times, filename)
    elif format == "sparse":
        _export_spikes_sparse(result.spike_times, result.duration, result.dt, filename)
    else:
        raise ValueError(f"Unknown format: {format}")


def _export_spikes_csv(spike_times: Dict[str, List[float]], filename: str):
    """Export spikes as CSV with columns: time, neuron_id."""
    rows = []
    for nid, times in spike_times.items():
        for t in times:
            rows.append((t, nid))

    # Sort by time
    rows.sort(key=lambda x: x[0])

    with open(f"{filename}.csv", 'w') as f:
        f.write("time_ms,neuron_id\n")
        for t, nid in rows:
            f.write(f"{t},{nid}\n")


def _export_spikes_json(spike_times: Dict[str, List[float]], filename: str):
    """Export spikes as JSON dictionary."""
    output = {
        nid: list(times) for nid, times in spike_times.items()
    }
    with open(f"{filename}.json", 'w') as f:
        json.dump(output, f, indent=2)


def _export_spikes_sparse(
    spike_times: Dict[str, List[float]],
    duration: float,
    dt: float,
    filename: str
):
    """Export spikes as sparse binary matrix."""
    neuron_ids = sorted(spike_times.keys())
    id_to_idx = {nid: i for i, nid in enumerate(neuron_ids)}

    n_neurons = len(neuron_ids)
    n_bins = int(duration / dt)

    # Collect spike indices
    time_indices = []
    neuron_indices = []

    for nid, times in spike_times.items():
        neuron_idx = id_to_idx[nid]
        for t in times:
            time_idx = int(t / dt)
            if 0 <= time_idx < n_bins:
                time_indices.append(time_idx)
                neuron_indices.append(neuron_idx)

    # Save as numpy archive with sparse representation
    np.savez(
        f"{filename}.npz",
        time_indices=np.array(time_indices, dtype=np.int32),
        neuron_indices=np.array(neuron_indices, dtype=np.int32),
        neuron_ids=np.array(neuron_ids, dtype=object),
        shape=np.array([n_bins, n_neurons]),
        dt=dt,
        duration=duration,
    )


def create_raster_data(
    spike_times: Dict[str, List[float]],
    neuron_order: Optional[List[str]] = None
) -> tuple:
    """
    Create data suitable for raster plots.

    Args:
        spike_times: Dictionary mapping neuron IDs to spike times
        neuron_order: Optional ordering of neurons (None = alphabetical)

    Returns:
        Tuple of (times, neuron_indices, neuron_ids)
    """
    if neuron_order is None:
        neuron_ids = sorted(spike_times.keys())
    else:
        neuron_ids = neuron_order

    id_to_idx = {nid: i for i, nid in enumerate(neuron_ids)}

    times = []
    indices = []

    for nid, spike_t in spike_times.items():
        if nid in id_to_idx:
            idx = id_to_idx[nid]
            for t in spike_t:
                times.append(t)
                indices.append(idx)

    return np.array(times), np.array(indices), neuron_ids


def compute_firing_rate_histogram(
    spike_times: Dict[str, List[float]],
    duration: float,
    bin_width: float = 10.0
) -> tuple:
    """
    Compute population firing rate histogram.

    Args:
        spike_times: Dictionary of spike times
        duration: Total simulation duration (ms)
        bin_width: Histogram bin width (ms)

    Returns:
        Tuple of (bin_centers, rates)
    """
    # Collect all spikes
    all_spikes = []
    for times in spike_times.values():
        all_spikes.extend(times)

    if not all_spikes:
        n_bins = int(duration / bin_width)
        return np.arange(bin_width/2, duration, bin_width), np.zeros(n_bins)

    all_spikes = np.array(all_spikes)

    # Create histogram
    n_bins = int(duration / bin_width)
    hist, edges = np.histogram(all_spikes, bins=n_bins, range=(0, duration))

    # Convert to rate (spikes/s)
    n_neurons = len(spike_times)
    rates = hist / (bin_width / 1000) / n_neurons

    # Bin centers
    centers = (edges[:-1] + edges[1:]) / 2

    return centers, rates


def compute_isi_distribution(
    spike_times: Dict[str, List[float]],
    max_isi: float = 100.0,
    n_bins: int = 50
) -> tuple:
    """
    Compute inter-spike interval distribution.

    Args:
        spike_times: Dictionary of spike times
        max_isi: Maximum ISI to include (ms)
        n_bins: Number of histogram bins

    Returns:
        Tuple of (bin_centers, counts)
    """
    all_isis = []

    for times in spike_times.values():
        times = np.array(sorted(times))
        if len(times) > 1:
            isis = np.diff(times)
            all_isis.extend(isis[isis <= max_isi])

    if not all_isis:
        return np.linspace(0, max_isi, n_bins), np.zeros(n_bins)

    hist, edges = np.histogram(all_isis, bins=n_bins, range=(0, max_isi))
    centers = (edges[:-1] + edges[1:]) / 2

    return centers, hist
