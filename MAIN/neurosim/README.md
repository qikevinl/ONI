# NeuroSim

**Neural Network Simulator for ONI Framework**

NeuroSim is a biologically-inspired neural network simulation package designed for integration with the [ONI (Organic Neural Interface) Framework](https://github.com/qikevinl/ONI). It provides tools for modeling brain-like neural networks with realistic neuron models, synaptic connections, and network architectures.

## Features

### Neuron Models
- **LIF (Leaky Integrate-and-Fire)**: Simple, computationally efficient
- **Izhikevich**: Rich dynamics with multiple firing patterns (RS, FS, IB, CH, LTS, TC)
- **Hodgkin-Huxley**: Biophysically detailed with ion channel dynamics
- **Adaptive LIF/AdEx**: LIF with spike-frequency adaptation

### Synapse Models
- **Chemical Synapses**: AMPA, NMDA, GABA-A, GABA-B receptors
- **Electrical Synapses**: Gap junctions with optional rectification
- **STDP Synapses**: Spike-timing dependent plasticity for learning

### Network Architectures
- **Layered Networks**: Feedforward architectures, compatible with ONI 14-layer model
- **Recurrent Networks**: E/I balanced networks with feedback connections
- **Small-World Networks**: Watts-Strogatz topology with high clustering

### Simulation Engine
- Efficient time-stepped simulation
- Event-driven input handling
- Stimulus protocols (constant, pulse, Poisson noise)
- Real-time data recording

### Data Export
- ONI Framework native format
- NumPy arrays (.npz)
- JSON for web integration
- CSV for analysis tools

### User Interface
- **Web UI**: Streamlit-based interface for non-technical users
- **CLI**: Command-line interface for scripting and automation

## Installation

```bash
# Basic installation
pip install neurosim

# With web UI support
pip install neurosim[ui]

# Full installation with all dependencies
pip install neurosim[full]
```

Or install from source:
```bash
cd MAIN/neurosim
pip install -e .
```

## Quick Start

### Python API

```python
from neurosim import LIFNeuron, LayeredNetwork
from neurosim.engine import SimulationEngine, SimulationConfig

# Create a layered network
network = LayeredNetwork.create_simple(
    n_layers=3,
    neurons_per_layer=100
)

# Configure simulation
config = SimulationConfig(
    duration=1000,  # ms
    dt=0.1,         # ms
    verbose=True
)

# Run simulation
engine = SimulationEngine(network, config)

# Add input to first layer
for nid in list(network.neurons.keys())[:10]:
    engine.add_input_current(nid, 5.0)  # 5 nA

result = engine.run()

# Analyze results
print(f"Total spikes: {result.total_spikes}")
print(f"Mean firing rate: {result.mean_firing_rate:.2f} Hz")
```

### Web UI

Launch the interactive web interface:

```bash
neurosim ui
```

Then open http://localhost:8501 in your browser.

### Command Line

```bash
# Run a simulation
neurosim run --network layered --layers 3 --neurons 100 --duration 1000

# Run with ONI 14-layer model
neurosim run --network oni --duration 2000 --output oni_simulation

# Export to different formats
neurosim export results.npz --format json
```

## ONI Framework Integration

NeuroSim is designed to generate simulated neural data compatible with the ONI Framework's 14-layer neural security model.

```python
from neurosim import LayeredNetwork
from neurosim.engine import SimulationEngine, SimulationConfig
from neurosim.export import ONIExporter, ONIDataFormat

# Create ONI 14-layer model network
network = LayeredNetwork.create_oni_model(neurons_per_layer=50)

# Run simulation
config = SimulationConfig(duration=2000)
engine = SimulationEngine(network, config)
result = engine.run()

# Export for ONI Framework
exporter = ONIExporter()
oni_data = exporter.export(result, network)
exporter.save(oni_data, "simulation_oni.json", ONIDataFormat.ONI_NATIVE)

# Access layer-specific metrics
for layer_id, metrics in oni_data.layers.items():
    print(f"Layer {layer_id} ({metrics.name}):")
    print(f"  Neurons: {metrics.n_neurons}")
    print(f"  Firing rate: {metrics.mean_rate:.2f} Hz")
    print(f"  Coherence: {metrics.coherence:.3f}")
```

## Network Types

### Layered Network

```python
from neurosim import LayeredNetwork
from neurosim.core.networks.layered import LayeredNetworkParameters

# Custom layered network
params = LayeredNetworkParameters(
    n_layers=5,
    neurons_per_layer=50,
    feedforward_prob=0.3,
    lateral_connections=True,
)
network = LayeredNetwork(params)

# Pre-configured ONI model
network = LayeredNetwork.create_oni_model()
```

### Recurrent Network

```python
from neurosim import RecurrentNetwork

# Balanced E/I network
network = RecurrentNetwork.create_balanced(n_neurons=1000, g=4.0)

# With STDP plasticity
network = RecurrentNetwork.create_plastic(n_neurons=500, stdp_lr=0.01)
```

### Small-World Network

```python
from neurosim import SmallWorldNetwork

# Watts-Strogatz topology
network = SmallWorldNetwork.create_watts_strogatz(
    n=500,   # neurons
    k=4,     # local neighbors
    p=0.1    # rewiring probability
)

# Cortical-like module
network = SmallWorldNetwork.create_cortical_module(n_neurons=200)
```

## Neuron Models

### LIF Neuron

```python
from neurosim import LIFNeuron
from neurosim.core.neurons.lif import LIFParameters

# Custom parameters
params = LIFParameters(
    tau_m=20.0,        # Membrane time constant (ms)
    V_rest=-65.0,      # Resting potential (mV)
    V_threshold=-50.0, # Spike threshold (mV)
    t_refractory=2.0,  # Refractory period (ms)
)
neuron = LIFNeuron(params)

# Pre-configured types
exc_neuron = LIFNeuron.create_excitatory()
inh_neuron = LIFNeuron.create_inhibitory()
```

### Izhikevich Neuron

```python
from neurosim import IzhikevichNeuron
from neurosim.core.neurons.izhikevich import IzhikevichType

# Different firing patterns
rs_neuron = IzhikevichNeuron.from_preset(IzhikevichType.RS)   # Regular spiking
fs_neuron = IzhikevichNeuron.from_preset(IzhikevichType.FS)   # Fast spiking
ib_neuron = IzhikevichNeuron.from_preset(IzhikevichType.IB)   # Intrinsically bursting
ch_neuron = IzhikevichNeuron.from_preset(IzhikevichType.CH)   # Chattering
```

### Hodgkin-Huxley Neuron

```python
from neurosim import HodgkinHuxleyNeuron

# Classic squid axon parameters
neuron = HodgkinHuxleyNeuron.create_squid_axon()

# Mammalian parameters (37°C)
neuron = HodgkinHuxleyNeuron.create_mammalian()
```

## Synapse Types

### Chemical Synapses

```python
from neurosim.core.synapses import ChemicalSynapse

# AMPA (fast excitatory)
synapse = ChemicalSynapse.create_ampa(pre, post, weight=1.0)

# GABA (fast inhibitory)
synapse = ChemicalSynapse.create_gaba(pre, post, weight=1.0)

# NMDA (slow excitatory)
synapse = ChemicalSynapse.create_nmda(pre, post, weight=0.5)
```

### STDP Synapses

```python
from neurosim.core.synapses import STDPSynapse

# Classic Hebbian STDP
synapse = STDPSynapse.create_hebbian(pre, post)

# Reward-modulated STDP
synapse = STDPSynapse.create_reward_modulated(pre, post)

# Apply reward signal
synapse.apply_reward(reward=1.0)
```

## Recording and Analysis

```python
from neurosim.engine import Recorder, RecordingConfig

# Configure recording
rec_config = RecordingConfig(
    variables=["voltage", "spike_times"],
    sample_every=1,  # Record every step
)

# After simulation
recorder = engine.recorder

# Get spike raster data
times, indices = recorder.get_raster_data()

# Compute firing rates
rates = recorder.compute_firing_rates(window=100)

# Get population rate
t, pop_rate = recorder.compute_population_rate()
```

## Configuration Files

Run simulations from JSON configuration:

```json
{
    "network_type": "layered",
    "n_layers": 5,
    "neurons_per_layer": 100,
    "duration": 2000,
    "dt": 0.1,
    "inputs": {
        "type": "constant",
        "amplitude": 5.0,
        "target_fraction": 0.1
    },
    "output": {
        "format": "oni",
        "filename": "simulation_output"
    }
}
```

```bash
neurosim run --config simulation.json
```

## Architecture

```
neurosim/
├── core/
│   ├── neurons/          # Neuron models
│   │   ├── lif.py
│   │   ├── izhikevich.py
│   │   ├── hodgkin_huxley.py
│   │   └── adaptive_lif.py
│   ├── synapses/         # Synapse models
│   │   ├── chemical.py
│   │   ├── electrical.py
│   │   └── stdp.py
│   └── networks/         # Network architectures
│       ├── layered.py
│       ├── recurrent.py
│       └── small_world.py
├── engine/               # Simulation engine
│   ├── simulator.py
│   ├── events.py
│   └── recorder.py
├── export/               # Data export
│   ├── oni_export.py
│   └── formats.py
├── ui/                   # Streamlit web UI
│   └── app.py
└── cli/                  # Command-line interface
    └── main.py
```

## Use Cases

### 1. Neural Security Research
Generate simulated neural data for testing ONI Framework's security mechanisms.

### 2. Computational Neuroscience
Study network dynamics, plasticity, and information processing.

### 3. ONI Attack Simulation
Create adversarial neural patterns for security testing.

### 4. Education
Learn about neural networks with interactive visualization.

## Contributing

Contributions are welcome! Please see the [ONI Framework contributing guidelines](https://github.com/qikevinl/ONI/blob/main/CONTRIBUTING.md).

## License

Apache 2.0 - See [LICENSE](https://github.com/qikevinl/ONI/blob/main/LICENSE)

## Related Projects

- [ONI Framework](https://github.com/qikevinl/ONI) - Organic Neural Interface security framework
- [oni-framework](https://pypi.org/project/oni-framework/) - ONI Python package
