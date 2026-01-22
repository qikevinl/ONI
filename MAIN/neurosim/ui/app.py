"""
NeuroSim Streamlit Web Application

Interactive web interface for neural simulations.
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
from io import BytesIO
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def main():
    """Main Streamlit application."""

    st.set_page_config(
        page_title="NeuroSim - Neural Network Simulator",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Title and description
    st.title("🧠 NeuroSim")
    st.markdown("""
    **Neural Network Simulator for ONI Framework**

    Create and simulate biologically-inspired neural networks.
    Configure networks, run simulations, and analyze results - no coding required!
    """)

    # Sidebar configuration
    st.sidebar.header("Configuration")

    # Network type selection
    network_type = st.sidebar.selectbox(
        "Network Architecture",
        ["Layered Network", "Recurrent Network", "Small-World Network"],
        help="Choose the type of neural network to simulate"
    )

    # Simulation parameters
    st.sidebar.subheader("Simulation Settings")

    duration = st.sidebar.slider(
        "Duration (ms)",
        min_value=100,
        max_value=5000,
        value=1000,
        step=100,
        help="How long to run the simulation"
    )

    dt = st.sidebar.select_slider(
        "Time Step (ms)",
        options=[0.01, 0.05, 0.1, 0.5, 1.0],
        value=0.1,
        help="Simulation time resolution"
    )

    # Network-specific parameters
    st.sidebar.subheader("Network Parameters")

    if network_type == "Layered Network":
        n_layers = st.sidebar.slider("Number of Layers", 2, 14, 3)
        neurons_per_layer = st.sidebar.slider("Neurons per Layer", 10, 200, 50)
        use_oni_layers = st.sidebar.checkbox("Use ONI 14-Layer Model", value=False)
        connection_prob = st.sidebar.slider("Connection Probability", 0.1, 1.0, 0.3)

    elif network_type == "Recurrent Network":
        n_excitatory = st.sidebar.slider("Excitatory Neurons", 50, 500, 200)
        n_inhibitory = st.sidebar.slider("Inhibitory Neurons", 10, 200, 50)
        use_stdp = st.sidebar.checkbox("Enable STDP Learning", value=False)

    else:  # Small-World
        n_neurons = st.sidebar.slider("Total Neurons", 50, 500, 200)
        k_neighbors = st.sidebar.slider("Local Neighbors (k)", 2, 10, 4)
        p_rewire = st.sidebar.slider("Rewiring Probability (p)", 0.0, 0.5, 0.1)

    # Input settings
    st.sidebar.subheader("Input Current")

    input_type = st.sidebar.selectbox(
        "Input Type",
        ["Constant", "Pulse", "Poisson Noise", "None"]
    )

    if input_type != "None":
        input_amplitude = st.sidebar.slider(
            "Amplitude (nA)",
            0.0, 10.0, 2.0,
            help="Strength of input current"
        )

        if input_type == "Pulse":
            pulse_duration = st.sidebar.slider("Pulse Duration (ms)", 10, 500, 100)
            pulse_frequency = st.sidebar.slider("Pulse Frequency (Hz)", 1, 50, 10)

        if input_type == "Poisson Noise":
            noise_rate = st.sidebar.slider("Noise Rate (Hz)", 1, 100, 20)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Network Visualization")

        # Placeholder for network diagram
        if st.button("🔄 Create Network", type="primary"):
            with st.spinner("Creating neural network..."):
                network, network_info = create_network(
                    network_type,
                    locals()
                )
                st.session_state['network'] = network
                st.session_state['network_info'] = network_info

        if 'network' in st.session_state:
            info = st.session_state['network_info']
            st.success(f"Network created: {info['n_neurons']} neurons, {info['n_synapses']} synapses")

            # Display network visualization
            fig = create_network_visualization(st.session_state['network'], network_type)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Network Summary")

        if 'network_info' in st.session_state:
            info = st.session_state['network_info']
            st.metric("Neurons", info['n_neurons'])
            st.metric("Synapses", info['n_synapses'])
            st.metric("Architecture", info['type'])

            if 'layers' in info:
                st.write(f"**Layers:** {info['layers']}")

    # Simulation section
    st.markdown("---")
    st.subheader("Run Simulation")

    if 'network' not in st.session_state:
        st.info("Create a network first to run simulations")
    else:
        col_sim1, col_sim2, col_sim3 = st.columns([1, 1, 2])

        with col_sim1:
            if st.button("▶️ Run Simulation", type="primary"):
                with st.spinner(f"Simulating {duration}ms..."):
                    result = run_simulation(
                        st.session_state['network'],
                        duration=duration,
                        dt=dt,
                        input_type=input_type,
                        input_params=locals()
                    )
                    st.session_state['result'] = result

        with col_sim2:
            if 'result' in st.session_state:
                st.success("Simulation complete!")

        with col_sim3:
            if 'result' in st.session_state:
                result = st.session_state['result']
                st.metric("Total Spikes", result['total_spikes'])
                st.metric("Mean Rate", f"{result['mean_rate']:.1f} Hz")

    # Results visualization
    if 'result' in st.session_state:
        st.markdown("---")
        st.subheader("Results")

        result = st.session_state['result']

        # Tabs for different visualizations
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Raster Plot",
            "📈 Voltage Traces",
            "📉 Firing Rates",
            "📁 Export Data"
        ])

        with tab1:
            fig_raster = create_raster_plot(result)
            st.plotly_chart(fig_raster, use_container_width=True)

        with tab2:
            # Select neurons to display
            neuron_ids = list(result.get('voltages', {}).keys())[:10]
            if neuron_ids:
                selected_neurons = st.multiselect(
                    "Select neurons to display",
                    neuron_ids,
                    default=neuron_ids[:3]
                )
                if selected_neurons:
                    fig_voltage = create_voltage_plot(result, selected_neurons)
                    st.plotly_chart(fig_voltage, use_container_width=True)
            else:
                st.info("No voltage data recorded")

        with tab3:
            fig_rates = create_firing_rate_plot(result)
            st.plotly_chart(fig_rates, use_container_width=True)

        with tab4:
            st.write("Download simulation results:")

            col_exp1, col_exp2 = st.columns(2)

            with col_exp1:
                # JSON export
                json_data = export_to_json(result)
                st.download_button(
                    "📄 Download JSON",
                    data=json_data,
                    file_name="neurosim_results.json",
                    mime="application/json"
                )

            with col_exp2:
                # CSV spike export
                csv_data = export_spikes_csv(result)
                st.download_button(
                    "📊 Download Spikes (CSV)",
                    data=csv_data,
                    file_name="neurosim_spikes.csv",
                    mime="text/csv"
                )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
    NeuroSim - Part of the ONI Framework |
    <a href="https://github.com/qikevinl/ONI">GitHub</a>
    </div>
    """, unsafe_allow_html=True)


def create_network(network_type: str, params: dict):
    """Create a neural network based on user configuration."""
    try:
        from neurosim.core.networks import LayeredNetwork, RecurrentNetwork, SmallWorldNetwork
        from neurosim.core.networks.layered import LayeredNetworkParameters
        from neurosim.core.networks.recurrent import RecurrentNetworkParameters
        from neurosim.core.networks.small_world import SmallWorldParameters
    except ImportError:
        # Fallback for demo mode
        return create_demo_network(network_type, params)

    if network_type == "Layered Network":
        if params.get('use_oni_layers', False):
            network = LayeredNetwork.create_oni_model(
                neurons_per_layer=params.get('neurons_per_layer', 50)
            )
        else:
            network_params = LayeredNetworkParameters(
                n_layers=params.get('n_layers', 3),
                neurons_per_layer=params.get('neurons_per_layer', 50),
                feedforward_prob=params.get('connection_prob', 0.3),
            )
            network = LayeredNetwork(network_params)

        info = {
            'type': 'Layered',
            'n_neurons': network.n_neurons,
            'n_synapses': network.n_synapses,
            'layers': network.n_layers,
        }

    elif network_type == "Recurrent Network":
        network_params = RecurrentNetworkParameters(
            n_excitatory=params.get('n_excitatory', 200),
            n_inhibitory=params.get('n_inhibitory', 50),
            use_stdp=params.get('use_stdp', False),
        )
        network = RecurrentNetwork(network_params)

        info = {
            'type': 'Recurrent',
            'n_neurons': network.n_neurons,
            'n_synapses': network.n_synapses,
        }

    else:  # Small-World
        network_params = SmallWorldParameters(
            n_neurons=params.get('n_neurons', 200),
            k=params.get('k_neighbors', 4),
            p_rewire=params.get('p_rewire', 0.1),
        )
        network = SmallWorldNetwork(network_params)

        info = {
            'type': 'Small-World',
            'n_neurons': network.n_neurons,
            'n_synapses': network.n_synapses,
        }

    return network, info


def create_demo_network(network_type: str, params: dict):
    """Create a demo network when full imports aren't available."""
    # Demo mode - return mock data
    if network_type == "Layered Network":
        n_layers = params.get('n_layers', 3)
        neurons_per_layer = params.get('neurons_per_layer', 50)
        n_neurons = n_layers * neurons_per_layer
        n_synapses = int(n_neurons * neurons_per_layer * params.get('connection_prob', 0.3))
        info = {
            'type': 'Layered (Demo)',
            'n_neurons': n_neurons,
            'n_synapses': n_synapses,
            'layers': n_layers,
        }
    elif network_type == "Recurrent Network":
        n_neurons = params.get('n_excitatory', 200) + params.get('n_inhibitory', 50)
        n_synapses = int(n_neurons * n_neurons * 0.1)
        info = {
            'type': 'Recurrent (Demo)',
            'n_neurons': n_neurons,
            'n_synapses': n_synapses,
        }
    else:
        n_neurons = params.get('n_neurons', 200)
        n_synapses = n_neurons * params.get('k_neighbors', 4) * 2
        info = {
            'type': 'Small-World (Demo)',
            'n_neurons': n_neurons,
            'n_synapses': n_synapses,
        }

    return {'demo': True, 'info': info}, info


def run_simulation(network, duration: float, dt: float, input_type: str, input_params: dict):
    """Run the neural simulation."""
    try:
        from neurosim.engine import SimulationEngine, SimulationConfig
    except ImportError:
        # Demo mode
        return run_demo_simulation(network, duration, dt, input_type, input_params)

    if isinstance(network, dict) and network.get('demo'):
        return run_demo_simulation(network, duration, dt, input_type, input_params)

    config = SimulationConfig(
        duration=duration,
        dt=dt,
        verbose=False,
    )

    engine = SimulationEngine(network, config)

    # Add inputs
    if input_type == "Constant":
        amplitude = input_params.get('input_amplitude', 2.0)
        for nid in list(network.neurons.keys())[:int(network.n_neurons * 0.1)]:
            engine.add_input_current(nid, amplitude)

    result = engine.run()

    return {
        'total_spikes': result.total_spikes,
        'mean_rate': result.mean_firing_rate,
        't': result.t,
        'voltages': result.voltages or {},
        'spike_times': result.spike_times or {},
        'spike_counts': result.spike_counts or {},
    }


def run_demo_simulation(network, duration: float, dt: float, input_type: str, input_params: dict):
    """Run a demo simulation with synthetic data."""
    n_steps = int(duration / dt)
    t = np.arange(0, duration, dt)

    info = network.get('info', {})
    n_neurons = info.get('n_neurons', 100)

    # Generate synthetic spike data
    spike_times = {}
    spike_counts = {}
    total_spikes = 0

    base_rate = 10 if input_type == "None" else 30  # Hz

    for i in range(min(n_neurons, 50)):  # Limit for demo
        nid = f"neuron_{i}"
        rate = base_rate + np.random.uniform(-5, 5)
        n_spikes = int(rate * duration / 1000)
        spikes = np.sort(np.random.uniform(0, duration, n_spikes))
        spike_times[nid] = list(spikes)
        spike_counts[nid] = len(spikes)
        total_spikes += len(spikes)

    # Generate synthetic voltage traces
    voltages = {}
    for i in range(min(10, n_neurons)):
        nid = f"neuron_{i}"
        v = -65 + np.random.randn(n_steps) * 5
        # Add spikes
        for spike_t in spike_times.get(nid, []):
            idx = int(spike_t / dt)
            if 0 <= idx < n_steps - 5:
                v[idx:idx+3] = [0, 30, -70]
        voltages[nid] = v

    mean_rate = total_spikes / n_neurons / (duration / 1000) if n_neurons > 0 else 0

    return {
        'total_spikes': total_spikes,
        'mean_rate': mean_rate,
        't': t,
        'voltages': voltages,
        'spike_times': spike_times,
        'spike_counts': spike_counts,
    }


def create_network_visualization(network, network_type: str):
    """Create a visualization of the network structure."""
    fig = go.Figure()

    if isinstance(network, dict) and network.get('demo'):
        info = network.get('info', {})
        # Simple demo visualization
        n_neurons = info.get('n_neurons', 100)

        if 'layers' in info:
            # Layered visualization
            n_layers = info['layers']
            neurons_per_layer = n_neurons // n_layers

            for layer in range(n_layers):
                x = [layer] * min(neurons_per_layer, 20)
                y = list(range(min(neurons_per_layer, 20)))
                fig.add_trace(go.Scatter(
                    x=x, y=y,
                    mode='markers',
                    marker=dict(size=10, color=layer, colorscale='Viridis'),
                    name=f'Layer {layer + 1}'
                ))
        else:
            # Random positions for other types
            n_display = min(n_neurons, 50)
            x = np.random.randn(n_display)
            y = np.random.randn(n_display)
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='markers',
                marker=dict(size=10, color='blue'),
                name='Neurons'
            ))
    else:
        # Real network visualization
        try:
            positions = []
            for nid, neuron in network.neurons.items():
                if hasattr(neuron.params, 'position') and neuron.params.position:
                    positions.append(neuron.params.position[:2])
                else:
                    positions.append((np.random.randn(), np.random.randn()))

            positions = np.array(positions)
            fig.add_trace(go.Scatter(
                x=positions[:, 0],
                y=positions[:, 1],
                mode='markers',
                marker=dict(size=8, color='blue'),
                name='Neurons'
            ))
        except Exception:
            pass

    fig.update_layout(
        title="Network Structure",
        xaxis_title="Position",
        yaxis_title="Position",
        showlegend=True,
        height=400,
    )

    return fig


def create_raster_plot(result: dict):
    """Create a spike raster plot."""
    fig = go.Figure()

    spike_times = result.get('spike_times', {})
    neuron_ids = sorted(spike_times.keys())

    for i, nid in enumerate(neuron_ids[:50]):  # Limit display
        times = spike_times[nid]
        fig.add_trace(go.Scatter(
            x=times,
            y=[i] * len(times),
            mode='markers',
            marker=dict(size=2, color='black'),
            name=nid,
            showlegend=False
        ))

    fig.update_layout(
        title="Spike Raster Plot",
        xaxis_title="Time (ms)",
        yaxis_title="Neuron Index",
        height=400,
    )

    return fig


def create_voltage_plot(result: dict, neuron_ids: list):
    """Create voltage trace plots."""
    fig = go.Figure()

    t = result.get('t', [])
    voltages = result.get('voltages', {})

    for nid in neuron_ids:
        if nid in voltages:
            fig.add_trace(go.Scatter(
                x=t,
                y=voltages[nid],
                mode='lines',
                name=nid
            ))

    fig.update_layout(
        title="Membrane Potential",
        xaxis_title="Time (ms)",
        yaxis_title="Voltage (mV)",
        height=400,
    )

    return fig


def create_firing_rate_plot(result: dict):
    """Create population firing rate plot."""
    spike_times = result.get('spike_times', {})
    t = result.get('t', np.array([]))

    if len(t) == 0:
        return go.Figure()

    duration = t[-1]
    bin_width = 10  # ms
    n_bins = int(duration / bin_width)

    # Collect all spikes
    all_spikes = []
    for times in spike_times.values():
        all_spikes.extend(times)

    if not all_spikes:
        return go.Figure()

    # Create histogram
    hist, edges = np.histogram(all_spikes, bins=n_bins, range=(0, duration))
    centers = (edges[:-1] + edges[1:]) / 2

    # Convert to rate
    n_neurons = len(spike_times)
    rates = hist / (bin_width / 1000) / max(n_neurons, 1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=centers,
        y=rates,
        mode='lines',
        fill='tozeroy',
        name='Population Rate'
    ))

    fig.update_layout(
        title="Population Firing Rate",
        xaxis_title="Time (ms)",
        yaxis_title="Rate (Hz)",
        height=400,
    )

    return fig


def export_to_json(result: dict) -> str:
    """Export results to JSON string."""
    export_data = {
        'summary': {
            'total_spikes': result.get('total_spikes', 0),
            'mean_firing_rate_hz': result.get('mean_rate', 0),
        },
        'spike_times': {k: list(v) for k, v in result.get('spike_times', {}).items()},
        'spike_counts': result.get('spike_counts', {}),
    }
    return json.dumps(export_data, indent=2)


def export_spikes_csv(result: dict) -> str:
    """Export spike times to CSV string."""
    lines = ["time_ms,neuron_id"]
    for nid, times in result.get('spike_times', {}).items():
        for t in times:
            lines.append(f"{t},{nid}")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
