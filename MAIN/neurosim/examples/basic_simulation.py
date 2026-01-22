#!/usr/bin/env python3
"""
Basic Simulation Example

Demonstrates the simplest way to create and run a neural network simulation.
"""

import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from neurosim import LIFNeuron, LayeredNetwork
from neurosim.engine import SimulationEngine, SimulationConfig


def main():
    print("NeuroSim Basic Simulation Example")
    print("=" * 40)

    # Step 1: Create a simple layered network
    print("\n1. Creating network...")
    network = LayeredNetwork.create_simple(
        n_layers=3,
        neurons_per_layer=50
    )
    print(f"   Created: {network.n_neurons} neurons, {network.n_synapses} synapses")

    # Step 2: Configure simulation
    print("\n2. Configuring simulation...")
    config = SimulationConfig(
        duration=500,    # 500 ms simulation
        dt=0.1,          # 0.1 ms time step
        verbose=True,
        seed=42          # For reproducibility
    )

    # Step 3: Create simulation engine
    engine = SimulationEngine(network, config)

    # Step 4: Add input current to some neurons in the first layer
    print("\n3. Adding input current...")
    first_layer_neurons = network.get_layer_neurons(0)
    n_input = min(10, len(first_layer_neurons))

    for neuron in first_layer_neurons[:n_input]:
        engine.add_input_current(neuron.id, current=5.0)  # 5 nA

    print(f"   Applied 5 nA to {n_input} neurons")

    # Step 5: Run simulation
    print("\n4. Running simulation...")
    result = engine.run()

    # Step 6: Analyze results
    print("\n5. Results:")
    print(f"   Total spikes: {result.total_spikes}")
    print(f"   Mean firing rate: {result.mean_firing_rate:.2f} Hz")
    print(f"   Wall time: {result.wall_time:.2f} seconds")

    # Show spike counts by layer
    print("\n   Spikes per layer:")
    for layer_idx in range(network.n_layers):
        layer_neurons = network.get_layer_neurons(layer_idx)
        layer_spikes = sum(
            result.spike_counts.get(n.id, 0)
            for n in layer_neurons
        )
        print(f"     Layer {layer_idx + 1}: {layer_spikes} spikes")

    # Step 7: Save results
    print("\n6. Saving results...")
    from neurosim.export import export_to_json
    export_to_json(result, "basic_simulation_output")
    print("   Saved to: basic_simulation_output.json")

    print("\nSimulation complete!")


if __name__ == "__main__":
    main()
