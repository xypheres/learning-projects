import os
import shutil
import sys

for root, dirs, files in os.walk("."):
    for name in files:
        if name.endswith("(1).png"):
            os.remove(name)
