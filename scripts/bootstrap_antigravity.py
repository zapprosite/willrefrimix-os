import os
import sys
import subprocess
import importlib.util
import importlib.metadata

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check_file(path):
    if os.path.exists(path):
        print(f"[{GREEN}OK{RESET}] File found: {path}")
        return True
    else:
        print(f"[{RED}FAIL{RESET}] File missing: {path}")
        return False

def check_package(package_name):
    if importlib.util.find_spec(package_name) is not None:
         print(f"[{GREEN}OK{RESET}] Package installed: {package_name}")
         print(f"    Version: {importlib.metadata.version(package_name) if importlib.util.find_spec('importlib.metadata') else 'Unknown'}")
         return True
    else:
        # Try to import directly to be sure (some packages have different spec names)
        try:
            __import__(package_name)
            print(f"[{GREEN}OK{RESET}] Package installed (import check): {package_name}")
            return True
        except ImportError:
            print(f"[{RED}FAIL{RESET}] Package missing: {package_name}")
            return False

def check_gpu():
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[{GREEN}OK{RESET}] GPU Detected: {result.stdout.strip()}")
            return True
        else:
            print(f"[{RED}FAIL{RESET}] nvidia-smi failed.")
            return False
    except FileNotFoundError:
        print(f"[{RED}FAIL{RESET}] nvidia-smi not found.")
        return False

def main():
    print(f"\n{GREEN}=== ANTIGRAVITY OS v2.1: BOOTSTRAP HEALTH CHECK ==={RESET}\n")
    
    # 1. Governance Files
    print("--- 1. GOVERNANCE FILES ---")
    files_ok = True
    files_ok &= check_file("/srv-2/willrefrimix-os/docs/TASKMASTER.md")
    files_ok &= check_file("/srv-2/willrefrimix-os/docs/PRD.md")
    files_ok &= check_file("/srv-2/willrefrimix-os/README.md")
    files_ok &= check_file("/srv-2/willrefrimix-os/agents/AGENTS.md")
    files_ok &= check_file("/srv-2/willrefrimix-os/.agents/steering.json")
    
    # 2. Dependencies
    print("\n--- 2. CRITICAL DEPENDENCIES ---")
    pkg_ok = True
    # Checking import names, not package names in requirements.txt if they differ
    pkg_ok &= check_package("crewai")
    pkg_ok &= check_package("langgraph")
    pkg_ok &= check_package("qdrant_client")
    pkg_ok &= check_package("fastapi")
    
    # 3. Hardware
    print("\n--- 3. HARDWARE ---")
    hw_ok = check_gpu()

    print("\n--- SUMMARY ---")
    if files_ok and pkg_ok and hw_ok:
        print(f"{GREEN}✅ SYSTEM READY FOR AGENT DEPLOYMENT{RESET}")
        sys.exit(0)
    else:
        print(f"{RED}❌ SYSTEM ARCHITECTURE INCOMPLETE{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
