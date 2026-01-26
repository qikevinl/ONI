"""
ONI Academy CLI - Command-line interface for the learning platform.
"""

import argparse
import sys


def main():
    """Main entry point for oni-academy CLI."""
    parser = argparse.ArgumentParser(
        prog="oni-academy",
        description="ONI Academy - Educational platform for neurosecurity",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List modules command
    list_parser = subparsers.add_parser("list", help="List available learning modules")

    # Info command
    info_parser = subparsers.add_parser("info", help="Show information about a module")
    info_parser.add_argument("module", help="Module name")

    # UI command
    ui_parser = subparsers.add_parser("ui", help="Launch interactive learning UI")
    ui_parser.add_argument("--port", type=int, default=8502, help="Port for UI server")

    args = parser.parse_args()

    if args.command == "list":
        from oni_academy import list_modules
        modules = list_modules()
        print("\nONI Academy - Available Learning Modules")
        print("=" * 40)
        for module in modules:
            print(f"  - {module}")
        print("\nUse 'oni-academy info <module>' for details")
        print("Use 'oni-academy ui' for interactive learning")

    elif args.command == "info":
        from oni_academy import get_course
        course = get_course(args.module)
        if course:
            print(f"\n{course.get('title', args.module)}")
            print("=" * 40)
            print(f"Description: {course.get('description', 'No description')}")
            if course.get('modules'):
                print(f"Modules: {', '.join(course['modules'])}")
        else:
            print(f"Module '{args.module}' not found. Use 'oni-academy list' to see available modules.")

    elif args.command == "ui":
        try:
            import streamlit.web.cli as stcli
            import os

            # Find the UI app
            ui_path = os.path.join(os.path.dirname(__file__), "ui", "app.py")
            if not os.path.exists(ui_path):
                print("UI module not yet implemented. Coming soon!")
                print("\nFor now, explore the interactive web tools at:")
                print("  https://qikevinl.github.io/ONI/visualizations/")
                sys.exit(0)

            sys.argv = ["streamlit", "run", ui_path, "--server.port", str(args.port)]
            stcli.main()
        except ImportError:
            print("Streamlit not installed. Install with: pip install oni-academy[ui]")
            sys.exit(1)

    else:
        parser.print_help()
        print("\n" + "=" * 50)
        print("ONI Academy - Neurosecurity Education Platform")
        print("=" * 50)
        print("\nQuick Start:")
        print("  oni-academy list     # See available modules")
        print("  oni-academy ui       # Launch interactive UI")
        print("\nWeb Tools (no installation required):")
        print("  https://qikevinl.github.io/ONI/visualizations/")


if __name__ == "__main__":
    main()
