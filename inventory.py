import shutil
import sys

# Check disk usage
total, used, free = shutil.disk_usage("/")
percent_used = (used / total) * 100

print("Disk usage:", round(percent_used, 2), "%")

# Decide health status
if percent_used > 90:
    print("Health check FAILED: disk almost full")
    sys.exit(1)
else:
    print("Health check PASSED")
    sys.exit(0)
