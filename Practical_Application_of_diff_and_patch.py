### Practical Application of diff and patch


# cp disk_usage.py disk_usage_original.py
# cp disk_usage.py disk_usage_fixed.py

#!/usr/bin/env python3

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabites_free = du.free / 2**30
    if percent_free < min_percent or gigabites_free < min_absolute:
        return False
    return True

# Check for at least 2GB and 10% free

if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: not enough disk space")
    return 1

print("Everything ok")
return 0


# chmod +x disk_usage_fixed.py
# ./disk_usage_fixed.py
"""
return 1
    ^^^^^^^^
SyntaxError: 'return' outside function

"""

#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabites_free = du.free / 2**30
    if percent_free < min_percent or gigabites_free < min_absolute:
        return False
    return True

# Check for at least 2GB and 10% free

if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)

# ./disk_usage_fixed.py
"""
ERROR: not enough disk space
"""


#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabites_free = du.free / 2**30
    if percent_free < min_percent or gigabites_free < min_absolute:
        return False
    return True

# Check for at least 2GB and 10% free

if not check_disk_usage("/", 2, 10):
    print("ERROR: not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)

# ./disk_usage_fixed.py
"""
Everything ok
"""


# diff disk_usage_original.py disk_usage_fixed.py > disk_usage.diff
# cat disk_usage.diff
"""
3a4
> import sys
18c19
< if not check_disk_usage("/", 2*2**30, 10):
---
> if not check_disk_usage("/", 2, 10):
20c21
<     return 1
---
>     sys.exit(1)
23c24
< return 0
\ No newline at end of file
---
> sys.exit(0)
\ No newline at end of file
"""

# patch disk_usage.py < disk_usage.diff
"""
patching file disk_usage.py
 """

# ./disk_usage.py