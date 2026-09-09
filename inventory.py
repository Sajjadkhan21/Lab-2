import sys

<<<<<<< HEAD
# Check disk usage
total, used, free = shutil.disk_usage("/")
percent_used = (used / total) * 100

print("Disk usage:", round(percent_used, 2), "%")
# Get memory info from /proc/meminfo
mem_info = {}
with open("/proc/meminfo") as f:
    for line in f:
        parts = line.split(":")
        key = parts[0].strip()
        value = int(parts[1].strip().split()[0])
        mem_info[key] = value

total_mem = mem_info["MemTotal"]
available_mem = mem_info["MemAvailable"]
used_mem = total_mem - available_mem
percent_used = (used_mem / total_mem) * 100

print("Memory usage:", round(percent_used, 2), "%")
>>>>>>> feature-memory-check

if percent_used > 90:
    print("Health check FAILED: disk almost full")
    sys.exit(1)
else:
    print("Health check PASSED")
    sys.exit(0)


