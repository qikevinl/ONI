#!/usr/bin/env python3
"""
Neuron Model Comparison

Compares different neuron models (LIF, Izhikevich, Hodgkin-Huxley)
to demonstrate their different dynamics and computational properties.
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from neurosim import LIFNeuron, IzhikevichNeuron, HodgkinHuxleyNeuron
from neurosim.core.neurons.izhikevich import IzhikevichType


def simulate_single_neuron(neuron, duration=200, input_current=10.0):
    """Simulate a single neuron with constant input."""
    dt = neuron.params.dt
    n_steps = int(duration / dt)

    # Create input current array
    current = np.ones(n_steps) * input_current

    # Run simulation
    results = neuron.simulate(duration, input_current=current)

    return results


def main():
    print("NeuroSim Neuron Model Comparison")
    print("=" * 50)

    duration = 200  # ms
    input_current = 10.0  # nA

    print(f"\nSimulation: {duration}ms with {input_current} nA input current")
    print("-" * 50)

    # 1. LIF Neuron
    print("\n1. Leaky Integrate-and-Fire (LIF)")
    lif = LIFNeuron.create_excitatory()
    lif_results = simulate_single_neuron(lif, duration, input_current)
    lif_spikes = len(lif_results["spike_times"])
    print(f"   Spikes: {lif_spikes}")
    print(f"   Firing rate: {lif_spikes / (duration/1000):.1f} Hz")
    print(f"   V range: [{lif_results['V'].min():.1f}, {lif_results['V'].max():.1f}] mV")

    # 2. Izhikevich - Regular Spiking
    print("\n2. Izhikevich (Regular Spiking)")
    izh_rs = IzhikevichNeuron.from_preset(IzhikevichType.RS)
    izh_rs_results = simulate_single_neuron(izh_rs, duration, input_current)
    izh_rs_spikes = len(izh_rs_results["spike_times"])
    print(f"   Spikes: {izh_rs_spikes}")
    print(f"   Firing rate: {izh_rs_spikes / (duration/1000):.1f} Hz")
    print(f"   V range: [{izh_rs_results['V'].min():.1f}, {izh_rs_results['V'].max():.1f}] mV")

    # 3. Izhikevich - Fast Spiking
    print("\n3. Izhikevich (Fast Spiking)")
    izh_fs = IzhikevichNeuron.from_preset(IzhikevichType.FS)
    izh_fs_results = simulate_single_neuron(izh_fs, duration, input_current)
    izh_fs_spikes = len(izh_fs_results["spike_times"])
    print(f"   Spikes: {izh_fs_spikes}")
    print(f"   Firing rate: {izh_fs_spikes / (duration/1000):.1f} Hz")
    print(f"   V range: [{izh_fs_results['V'].min():.1f}, {izh_fs_results['V'].max():.1f}] mV")

    # 4. Izhikevich - Intrinsically Bursting
    print("\n4. Izhikevich (Intrinsically Bursting)")
    izh_ib = IzhikevichNeuron.from_preset(IzhikevichType.IB)
    izh_ib_results = simulate_single_neuron(izh_ib, duration, input_current)
    izh_ib_spikes = len(izh_ib_results["spike_times"])
    print(f"   Spikes: {izh_ib_spikes}")
    print(f"   Firing rate: {izh_ib_spikes / (duration/1000):.1f} Hz")
    print(f"   V range: [{izh_ib_results['V'].min():.1f}, {izh_ib_results['V'].max():.1f}] mV")

    # 5. Hodgkin-Huxley
    print("\n5. Hodgkin-Huxley (Squid Axon)")
    hh = HodgkinHuxleyNeuron.create_squid_axon()
    hh_results = simulate_single_neuron(hh, duration, input_current)
    hh_spikes = len(hh_results["spike_times"])
    print(f"   Spikes: {hh_spikes}")
    print(f"   Firing rate: {hh_spikes / (duration/1000):.1f} Hz")
    print(f"   V range: [{hh_results['V'].min():.1f}, {hh_results['V'].max():.1f}] mV")

    # Summary comparison
    print("\n" + "=" * 50)
    print("Summary Comparison")
    print("-" * 50)
    print(f"{'Model':<25} {'Spikes':<10} {'Rate (Hz)':<12} {'Complexity':<12}")
    print("-" * 50)
    print(f"{'LIF':<25} {lif_spikes:<10} {lif_spikes/(duration/1000):<12.1f} {'Low':<12}")
    print(f"{'Izhikevich RS':<25} {izh_rs_spikes:<10} {izh_rs_spikes/(duration/1000):<12.1f} {'Medium':<12}")
    print(f"{'Izhikevich FS':<25} {izh_fs_spikes:<10} {izh_fs_spikes/(duration/1000):<12.1f} {'Medium':<12}")
    print(f"{'Izhikevich IB':<25} {izh_ib_spikes:<10} {izh_ib_spikes/(duration/1000):<12.1f} {'Medium':<12}")
    print(f"{'Hodgkin-Huxley':<25} {hh_spikes:<10} {hh_spikes/(duration/1000):<12.1f} {'High':<12}")

    print("\nNotes:")
    print("- LIF: Simple, fast, good for large networks")
    print("- Izhikevich: Balance of efficiency and biological realism")
    print("- Hodgkin-Huxley: Most realistic, computationally expensive")

    print("\nComparison complete!")


if __name__ == "__main__":
    main()
