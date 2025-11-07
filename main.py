import psutil
import time
from datetime import datetime

# ----------------------------------------------
# Configuration variables
# Tweak these values as needed

MAX_MB_ALLOWED = 1024 # Maximum memory allowed in MB, ⚠️ It's not recommended to set it below 512
CHECK_INTERVAL = 5 # Interval between checks in seconds
# ----------------------------------------------


# Private variables
print_message_on_next_check = False
MB_SQUARED = 1024 ** 2


def kill_biome_if_needed():
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        # Use the global variable to track message printing
        global print_message_on_next_check

        if print_message_on_next_check:
            print_watcher_message()
            print_message_on_next_check = False

        try:
            # Check if the process name contains "biome"
            name = proc.info["name"]
            if not name or not "biome" in name.lower():
                continue

            # Get memory usage in MB
            mem_mb = proc.info["memory_info"].rss / MB_SQUARED

            # If memory usage exceeds the limit, terminate the process
            if mem_mb > MAX_MB_ALLOWED:
                print_msg(f"💀 Killing {name} (PID {proc.pid}) using {mem_mb:.1f}MB")
                proc.terminate()
                print_message_on_next_check = True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print_msg("⚠️ Could not access process information.")
            pass

def print_watcher_message():
    print_msg("👀 Watching for biome.exe memory usage...")

def print_msg(msg: str):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{current_time}: {msg}")

def main():
    print("— 🛡️ Biome Leak Guard —")
    print_watcher_message()

    try:
        while True:
            kill_biome_if_needed()
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print_msg(f"❌ Process terminated by user.")


if __name__ == "__main__":
    main()
