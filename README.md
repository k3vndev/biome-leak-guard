# 🛡️ Biome Leak Guard

A simple Python script that monitors the memory usage of the `biome.exe` process from [biome](https://github.com/biomejs/biome) and terminates it if it exceeds a specified limit.

## Installation

1. Ensure you have Python and [UV](https://docs.astral.sh/uv) installed on your system.

2. Clone the repository:
    ```bash
      git clone https://github.com/k3vndev/biome-leak-guard
      cd biome-leak-guard
    ```

3. Install the required dependencies:
    ```bash
    uv sync
    pip install -e .
    ```

---

**Note:** If the script fails to run due to missing `psutil` module, you can manually install it using:
```bash
pip install psutil
```

## Usage

Run the script using Python:
```bash
blguard # Or just "blg"
```

It will continuously monitor the memory usage of `biome.exe` and terminate it if it exceeds the defined limit.

## Why?

The 2.2.2 version of Biome has a memory leak issue that can cause it to consume excessive amounts of RAM over time. Seen it happen multiple times where Biome would use over 10GB of RAM, making the system freeze and become unresponsive 💀

By default, this script is configured to terminate `biome.exe` if it exceeds **1024 MB (1 GB)** of memory usage. You can adjust this limit in the script as needed.


## Extra comments

- All the logic is contained in `main.py`.
- You can tweak the `MAX_MB_ALLOWED` and `CHECK_INTERVAL` constants in `main.py` to fit your needs.
- Make sure to run the script with appropriate permissions to allow it to monitor and terminate processes.
- The script is designed to run indefinitely until manually stopped (e.g., via Ctrl+C).
- Logs messages to the console for monitoring actions taken by the script.