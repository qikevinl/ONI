"""
NeuroSim Command-Line Interface

Main CLI module using argparse for command handling.
"""

import argparse
import sys
import json
from pathlib import Path


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="neurosim",
        description="NeuroSim - Neural Network Simulator for ONI Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  neurosim run --config simulation.json
  neurosim run --network layered --duration 1000
  neurosim ui
  neurosim export results.npz --format json

For more information, visit: https://github.com/qikevinl/ONI
        """
    )

    parser.add_argument(
        "--version",
        action="version",
        version="NeuroSim 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a simulation")
    run_parser.add_argument(
        "--config", "-c",
        type=str,
        help="Path to configuration JSON file"
    )
    run_parser.add_argument(
        "--network", "-n",
        type=str,
        choices=["layered", "recurrent", "small-world", "oni"],
        default="layered",
        help="Network type (default: layered)"
    )
    run_parser.add_argument(
        "--duration", "-d",
        type=float,
        default=1000.0,
        help="Simulation duration in ms (default: 1000)"
    )
    run_parser.add_argument(
        "--dt",
        type=float,
        default=0.1,
        help="Time step in ms (default: 0.1)"
    )
    run_parser.add_argument(
        "--neurons", "-N",
        type=int,
        default=100,
        help="Number of neurons (default: 100)"
    )
    run_parser.add_argument(
        "--layers", "-l",
        type=int,
        default=3,
        help="Number of layers for layered network (default: 3)"
    )
    run_parser.add_argument(
        "--output", "-o",
        type=str,
        default="neurosim_output",
        help="Output filename (without extension)"
    )
    run_parser.add_argument(
        "--format", "-f",
        type=str,
        choices=["json", "numpy", "oni"],
        default="json",
        help="Output format (default: json)"
    )
    run_parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress output"
    )
    run_parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility"
    )

    # UI command
    ui_parser = subparsers.add_parser("ui", help="Launch web UI")
    ui_parser.add_argument(
        "--port", "-p",
        type=int,
        default=8501,
        help="Port for Streamlit server (default: 8501)"
    )
    ui_parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Don't open browser automatically"
    )

    # Export command
    export_parser = subparsers.add_parser("export", help="Export simulation data")
    export_parser.add_argument(
        "input",
        type=str,
        help="Input file (numpy .npz or json)"
    )
    export_parser.add_argument(
        "--format", "-f",
        type=str,
        choices=["json", "csv", "oni"],
        default="json",
        help="Output format"
    )
    export_parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output filename"
    )

    # Info command
    info_parser = subparsers.add_parser("info", help="Show system information")

    # Parse arguments
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Dispatch to command handlers
    if args.command == "run":
        return cmd_run(args)
    elif args.command == "ui":
        return cmd_ui(args)
    elif args.command == "export":
        return cmd_export(args)
    elif args.command == "info":
        return cmd_info(args)

    return 0


def cmd_run(args):
    """Handle the 'run' command."""
    print("NeuroSim - Neural Network Simulator")
    print("=" * 40)

    # Load configuration from file if provided
    config = {}
    if args.config:
        config_path = Path(args.config)
        if not config_path.exists():
            print(f"Error: Config file not found: {args.config}")
            return 1

        with open(config_path) as f:
            config = json.load(f)
        print(f"Loaded configuration from: {args.config}")

    # Merge command-line arguments with config
    network_type = config.get("network_type", args.network)
    duration = config.get("duration", args.duration)
    dt = config.get("dt", args.dt)
    n_neurons = config.get("n_neurons", args.neurons)
    n_layers = config.get("n_layers", args.layers)
    seed = config.get("seed", args.seed)
    verbose = not args.quiet

    if verbose:
        print(f"\nConfiguration:")
        print(f"  Network type: {network_type}")
        print(f"  Duration: {duration} ms")
        print(f"  Time step: {dt} ms")
        print(f"  Neurons: {n_neurons}")
        if network_type in ["layered", "oni"]:
            print(f"  Layers: {n_layers}")
        print()

    # Create network
    try:
        network = create_network_from_args(
            network_type,
            n_neurons,
            n_layers,
            seed
        )
    except ImportError as e:
        print(f"Error importing NeuroSim modules: {e}")
        print("Make sure NeuroSim is properly installed.")
        return 1

    if verbose:
        print(f"Created network: {network.n_neurons} neurons, {network.n_synapses} synapses")

    # Run simulation
    try:
        from neurosim.engine import SimulationEngine, SimulationConfig

        sim_config = SimulationConfig(
            duration=duration,
            dt=dt,
            verbose=verbose,
            seed=seed,
        )

        engine = SimulationEngine(network, sim_config)
        result = engine.run()

    except ImportError as e:
        print(f"Error importing simulation engine: {e}")
        return 1

    # Export results
    output_file = args.output
    output_format = args.format

    if verbose:
        print(f"\nSaving results to: {output_file}.{output_format}")

    save_results(result, network, output_file, output_format)

    if verbose:
        print("\nSimulation Summary:")
        print(f"  Total spikes: {result.total_spikes}")
        print(f"  Mean firing rate: {result.mean_firing_rate:.2f} Hz")
        print(f"  Wall time: {result.wall_time:.2f} seconds")

    return 0


def create_network_from_args(network_type: str, n_neurons: int, n_layers: int, seed: int = None):
    """Create a network based on command-line arguments."""
    import numpy as np
    if seed is not None:
        np.random.seed(seed)

    if network_type == "layered":
        from neurosim.core.networks import LayeredNetwork
        from neurosim.core.networks.layered import LayeredNetworkParameters

        neurons_per_layer = max(n_neurons // n_layers, 10)
        params = LayeredNetworkParameters(
            n_layers=n_layers,
            neurons_per_layer=neurons_per_layer,
            seed=seed,
        )
        return LayeredNetwork(params)

    elif network_type == "oni":
        from neurosim.core.networks import LayeredNetwork
        return LayeredNetwork.create_oni_model(
            neurons_per_layer=max(n_neurons // 14, 10)
        )

    elif network_type == "recurrent":
        from neurosim.core.networks import RecurrentNetwork
        from neurosim.core.networks.recurrent import RecurrentNetworkParameters

        n_exc = int(n_neurons * 0.8)
        n_inh = n_neurons - n_exc
        params = RecurrentNetworkParameters(
            n_excitatory=n_exc,
            n_inhibitory=n_inh,
            seed=seed,
        )
        return RecurrentNetwork(params)

    elif network_type == "small-world":
        from neurosim.core.networks import SmallWorldNetwork
        from neurosim.core.networks.small_world import SmallWorldParameters

        params = SmallWorldParameters(
            n_neurons=n_neurons,
            seed=seed,
        )
        return SmallWorldNetwork(params)

    else:
        raise ValueError(f"Unknown network type: {network_type}")


def save_results(result, network, filename: str, format: str):
    """Save simulation results to file."""
    if format == "json":
        from neurosim.export import export_to_json
        export_to_json(result, filename)

    elif format == "numpy":
        from neurosim.export import export_to_numpy
        export_to_numpy(result, filename)

    elif format == "oni":
        from neurosim.export import ONIExporter, ONIDataFormat
        exporter = ONIExporter()
        data = exporter.export(result, network)
        exporter.save(data, f"{filename}.json", ONIDataFormat.ONI_NATIVE)


def cmd_ui(args):
    """Handle the 'ui' command - launch Streamlit web interface."""
    import subprocess
    import os

    ui_path = Path(__file__).parent.parent / "ui" / "app.py"

    if not ui_path.exists():
        print(f"Error: UI module not found at {ui_path}")
        return 1

    cmd = ["streamlit", "run", str(ui_path), "--server.port", str(args.port)]

    if args.no_browser:
        cmd.extend(["--server.headless", "true"])

    print(f"Starting NeuroSim Web UI on port {args.port}...")
    print(f"Open http://localhost:{args.port} in your browser")
    print("Press Ctrl+C to stop")

    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        print("Error: Streamlit not found. Install with: pip install streamlit")
        return 1
    except KeyboardInterrupt:
        print("\nUI stopped.")

    return 0


def cmd_export(args):
    """Handle the 'export' command."""
    import numpy as np

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1

    # Determine output filename
    if args.output:
        output_file = args.output
    else:
        output_file = input_path.stem + "_exported"

    # Load input data
    if input_path.suffix == ".npz":
        data = dict(np.load(input_path, allow_pickle=True))
        print(f"Loaded numpy archive: {len(data)} arrays")
    elif input_path.suffix == ".json":
        with open(input_path) as f:
            data = json.load(f)
        print(f"Loaded JSON data")
    else:
        print(f"Error: Unsupported input format: {input_path.suffix}")
        return 1

    # Export to requested format
    if args.format == "json":
        with open(f"{output_file}.json", 'w') as f:
            # Convert numpy arrays to lists
            export_data = {}
            for k, v in data.items():
                if hasattr(v, 'tolist'):
                    export_data[k] = v.tolist()
                else:
                    export_data[k] = v
            json.dump(export_data, f, indent=2)
        print(f"Exported to: {output_file}.json")

    elif args.format == "csv":
        # Export spike data to CSV
        if 'spike_times' in data:
            with open(f"{output_file}_spikes.csv", 'w') as f:
                f.write("time_ms,neuron_id\n")
                for nid, times in data['spike_times'].items():
                    for t in times:
                        f.write(f"{t},{nid}\n")
            print(f"Exported spikes to: {output_file}_spikes.csv")

    elif args.format == "oni":
        from neurosim.export import ONIExporter
        # Create mock result object
        class MockResult:
            pass
        result = MockResult()
        result.duration = data.get('duration', 1000)
        result.dt = data.get('dt', 0.1)
        result.spike_times = data.get('spike_times', {})
        result.total_spikes = sum(len(v) for v in result.spike_times.values())
        result.mean_firing_rate = data.get('mean_firing_rate', 0)
        result.voltages = data.get('voltages', {})
        result.spike_counts = data.get('spike_counts', {})
        result.n_neurons = len(result.spike_times)
        result.n_synapses = 0

        exporter = ONIExporter()
        # Export without network (limited functionality)
        export_data = {
            "metadata": {
                "format": "oni_neurosim_export",
                "duration_ms": result.duration,
            },
            "spike_data": {
                nid: list(times) for nid, times in result.spike_times.items()
            },
        }
        with open(f"{output_file}.oni.json", 'w') as f:
            json.dump(export_data, f, indent=2)
        print(f"Exported to ONI format: {output_file}.oni.json")

    return 0


def cmd_info(args):
    """Handle the 'info' command - show system information."""
    print("NeuroSim System Information")
    print("=" * 40)

    print("\nVersion: 0.1.0")

    # Python version
    print(f"\nPython: {sys.version}")

    # Check dependencies
    print("\nDependencies:")
    deps = [
        ("numpy", "numpy"),
        ("streamlit", "streamlit"),
        ("plotly", "plotly"),
    ]

    for name, module in deps:
        try:
            mod = __import__(module)
            version = getattr(mod, "__version__", "unknown")
            print(f"  {name}: {version}")
        except ImportError:
            print(f"  {name}: NOT INSTALLED")

    # Check NeuroSim modules
    print("\nNeuroSim Modules:")
    modules = [
        "neurosim.core",
        "neurosim.engine",
        "neurosim.export",
        "neurosim.ui",
    ]

    for mod_name in modules:
        try:
            __import__(mod_name)
            print(f"  {mod_name}: OK")
        except ImportError as e:
            print(f"  {mod_name}: MISSING ({e})")

    return 0


def cli():
    """CLI entry point for setuptools."""
    sys.exit(main())


if __name__ == "__main__":
    sys.exit(main())
