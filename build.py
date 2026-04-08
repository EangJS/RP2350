import os
import subprocess
import sys
import shutil

BUILD_DIR = "build"
BOARD = "pico2"
GENERATOR = "Ninja"


def run(command, cwd=None):
    print(f"\n>>> {' '.join(command)}\n")
    result = subprocess.run(command, cwd=cwd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def clean(build_path):
    if os.path.exists(build_path):
        print("🧹 Removing build directory...")
        shutil.rmtree(build_path)
        print("✅ Clean complete.")
    else:
        print("Nothing to clean.")


def configure_and_build(root, build_path):
    os.makedirs(build_path, exist_ok=True)

    # Configure with Ninja
    run([
        "cmake",
        "-S", root,
        "-B", build_path,
        "-G", GENERATOR,
        f"-DPICO_BOARD={BOARD}"
    ])

    # Build
    run([
        "cmake",
        "--build", build_path
    ])

    print("\n✅ Build complete using Ninja.")


def main():
    root = os.path.abspath(os.path.dirname(__file__))
    build_path = os.path.join(root, BUILD_DIR)

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "clean":
            clean(build_path)
            return

        else:
            print(f"Unknown command: {command}")
            print("Available commands: clean")
            sys.exit(1)

    configure_and_build(root, build_path)


if __name__ == "__main__":
    main()
