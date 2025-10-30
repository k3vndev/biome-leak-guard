import psutil
import time
from datetime import datetime

MAX_MB_ALLOWED = 1024
CHECK_INTERVAL = 5


def kill_biome_if_needed():
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            name = proc.info["name"]

            if name and "biome" in name.lower():
                mem_mb = proc.info["memory_info"].rss / (1024 * 1024)

                if mem_mb > MAX_MB_ALLOWED:
                    current_time = datetime.now().strftime("%H:%M:%S")

                    print(
                        f"{current_time}: 💀 Killing {name} (PID {proc.pid}) using {mem_mb:.1f}MB"
                    )
                    proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def main():
    print("✔️ We're keeping an eye over biome.exe")

    try:
        while True:
            kill_biome_if_needed()
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("❌ Process stopped.")


if __name__ == "__main__":
    main()
