#!/usr/bin/env python3
"""
ONI 14-Layer Model Simulation

Demonstrates how to create and simulate a network that maps to
the ONI Framework's 14-layer neural security model.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from neurosim import LayeredNetwork
from neurosim.engine import SimulationEngine, SimulationConfig
from neurosim.export import ONIExporter, ONIDataFormat


# ONI Layer descriptions
ONI_LAYERS = {
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


def main():
    print("NeuroSim ONI 14-Layer Model Simulation")
    print("=" * 50)

    # Step 1: Create ONI 14-layer network
    print("\n1. Creating ONI 14-layer model network...")
    network = LayeredNetwork.create_oni_model(
        neurons_per_layer=30  # Smaller for demo
    )
    print(f"   Created: {network.n_neurons} neurons, {network.n_synapses} synapses")
    print(f"   Layers: {network.n_layers}")

    # Show layer structure
    print("\n   Layer structure:")
    for layer_idx in range(min(network.n_layers, 14)):
        layer_neurons = network.get_layer_neurons(layer_idx)
        oni_layer = layer_idx + 1
        layer_name = ONI_LAYERS.get(oni_layer, f"Layer {oni_layer}")
        print(f"     {oni_layer:2d}. {layer_name}: {len(layer_neurons)} neurons")

    # Step 2: Configure simulation
    print("\n2. Configuring simulation (2 seconds)...")
    config = SimulationConfig(
        duration=2000,   # 2 second simulation
        dt=0.1,
        verbose=True,
        seed=123
    )

    engine = SimulationEngine(network, config)

    # Step 3: Add sensory input to Layer 1 (Physical Interface)
    print("\n3. Adding sensory input to Layer 1...")
    layer1_neurons = network.get_layer_neurons(0)
    n_input = min(10, len(layer1_neurons))

    for neuron in layer1_neurons[:n_input]:
        engine.add_input_current(neuron.id, current=8.0)

    print(f"   Applied input to {n_input} sensory neurons")

    # Step 4: Run simulation
    print("\n4. Running simulation...")
    result = engine.run()

    # Step 5: Export to ONI format
    print("\n5. Exporting to ONI format...")
    exporter = ONIExporter()
    oni_data = exporter.export(result, network)

    # Step 6: Display ONI metrics
    print("\n6. ONI Layer Metrics:")
    print("-" * 60)
    print(f"{'Layer':<30} {'Neurons':<10} {'Rate (Hz)':<12} {'Coherence':<10}")
    print("-" * 60)

    for layer_id in sorted(oni_data.layers.keys()):
        metrics = oni_data.layers[layer_id]
        print(f"{metrics.name:<30} {metrics.n_neurons:<10} {metrics.mean_rate:<12.2f} {metrics.coherence:<10.3f}")

    print("-" * 60)
    print(f"{'Global':<30} {oni_data.n_total_neurons:<10} {oni_data.mean_firing_rate:<12.2f} {oni_data.global_coherence:<10.3f}")

    # Step 7: Save ONI export
    print("\n7. Saving ONI export...")
    exporter.save(oni_data, "oni_simulation_output.json", ONIDataFormat.ONI_NATIVE)
    print("   Saved to: oni_simulation_output.json")

    # Step 8: Summary
    print("\n8. Summary:")
    print(f"   Total spikes: {result.total_spikes}")
    print(f"   Network synchrony: {oni_data.network_synchrony:.3f}")
    print(f"   Global coherence (Cs): {oni_data.global_coherence:.3f}")

    print("\nONI model simulation complete!")


if __name__ == "__main__":
    main()
