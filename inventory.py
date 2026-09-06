#!/usr/bin/env python3

import platform
import shutil

print("=== Server Inventory ===")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")

# Developer A:
# Add a disk usage section using shutil.disk_usage().

# Developer B:
# Add a memory section.
# On Linux you may read /proc/meminfo.

print("========================")
