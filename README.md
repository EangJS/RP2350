# RP2350 Project

This is a barebones project for the RP2350.

# Requirements

* SEGGER J-Link
* Python >= 3.12
* CMake >= 3.28.3
* Ninja >= v1.11.1

# Building

1. Clone this repository

2. Initalize all submodules using `git submodule update --init --recursive`

3. Run `python build.py` in the root directory of the project

# Flashing

Use SEGGER J-FLash to flash the generated binary at `build/pico_project.elf`
