import psutil
import time

MAX_MB_ALLOWED = 1024
CHECK_INTERVAL = 5


def kill_biome_if_needed():
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            name = proc.info["name"]

            if name and "biome" in name.lower():

                mem_mb = proc.info["memory_info"].rss / (1024 * 1024)
                if mem_mb > MAX_MB_ALLOWED:
                    print(f"💀 Killing {name} (PID {proc.pid}) using {mem_mb:.1f} MB")
                    proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def main():
    while True:
        kill_biome_if_needed()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
