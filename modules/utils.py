import subprocess
import shutil

def check_tools(required_tools):
    """Verifies if the required Go binaries are installed and in PATH."""
    missing_tools = []
    print("[*] Performing System Health Check...")
    
    for tool in required_tools:
        if shutil.which(tool) is None:
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"[!] Warning: The following tools are missing from your PATH: {', '.join(missing_tools)}")
        print("[!] Please install them for full functionality.")
        return False
    
    print("[+] All required tools found. System is healthy!")
    return True
