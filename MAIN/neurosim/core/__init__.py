"""
NeuroSim Core Module

Provides foundational components for neural simulation:
- Neuron models (LIF, Izhikevich, Hodgkin-Huxley)
- Synapse models (Chemical, Electrical, STDP)
- Network architectures (Feedforward, Recurrent, Layered)
"""

from .neurons import (
    Neuron,
    LIFNeuron,
    IzhikevichNeuron,
    HodgkinHuxleyNeuron,
    AdaptiveLIFNeuron,
)
from .synapses import (
    Synapse,
    ChemicalSynapse,
    ElectricalSynapse,
    STDPSynapse,
)
from .networks import (
    Network,
    LayeredNetwork,
    RecurrentNetwork,
    SmallWorldNetwork,
)

__all__ = [
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
]
