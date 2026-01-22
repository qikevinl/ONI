"""
NeuroSim - Neural Network Simulator for ONI Framework

A biologically-inspired neural network simulation package designed
for integration with the ONI (Organic Neural Interface) Framework.

Features:
- Multiple neuron models (LIF, Izhikevich, Hodgkin-Huxley)
- Chemical and electrical synapses with plasticity
- Various network architectures (Layered, Recurrent, Small-World)
- Event-driven simulation engine
- Data export for ONI Framework integration
- Web UI for non-technical users
- Command-line interface

Quick Start:
    >>> from neurosim import LIFNeuron, LayeredNetwork
    >>> from neurosim.engine import SimulationEngine, SimulationConfig

    >>> # Create a simple layered network
    >>> network = LayeredNetwork.create_simple(n_layers=3, neurons_per_layer=50)

    >>> # Run simulation
    >>> config = SimulationConfig(duration=1000)
    >>> engine = SimulationEngine(network, config)
    >>> result = engine.run()

    >>> print(f"Total spikes: {result.total_spikes}")

For the web UI:
    $ neurosim ui

For help:
    $ neurosim --help

License: Apache 2.0
"""

__version__ = "0.1.0"
__author__ = "ONI Framework Team"

# Core components
from .core import (
    # Neurons
    Neuron,
    LIFNeuron,
    IzhikevichNeuron,
    HodgkinHuxleyNeuron,
    AdaptiveLIFNeuron,
    # Synapses
    Synapse,
    ChemicalSynapse,
    ElectricalSynapse,
    STDPSynapse,
    # Networks
    Network,
    LayeredNetwork,
    RecurrentNetwork,
    SmallWorldNetwork,
)

# Simulation engine
from .engine import (
    SimulationEngine,
    SimulationConfig,
    Recorder,
    RecordingConfig,
)

# Export utilities
from .export import (
    ONIExporter,
    ONIDataFormat,
    export_to_numpy,
    export_to_json,
)

__all__ = [
    # Version
    "__version__",
    # Neurons
    "Neuron",
    "LIFNeuron",
    "IzhikevichNeuron",
    "HodgkinHuxleyNeuron",
    "AdaptiveLIFNeuron",
    # Synapses
    "Synapse",
    "ChemicalSynapse",
    "ElectricalSynapse",
    "STDPSynapse",
    # Networks
    "Network",
    "LayeredNetwork",
    "RecurrentNetwork",
    "SmallWorldNetwork",
    # Engine
    "SimulationEngine",
    "SimulationConfig",
    "Recorder",
    "RecordingConfig",
    # Export
    "ONIExporter",
    "ONIDataFormat",
    "export_to_numpy",
    "export_to_json",
]
