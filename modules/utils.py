import subprocess
import shutil
import os

def check_tools(required_tools):
    """Verifies if the required binaries are installed and in PATH (prioritizing local Go bins)."""
    missing_tools = []
    print("[*] Performing System Health Check...")
    
    # On Linux/CloudShell, prioritize ~/go/bin
    go_bin = os.path.expanduser("~/go/bin")
    
    for tool in required_tools:
        # Check system PATH first
        path = shutil.which(tool)
        
        # If not found or on Linux, check ~/go/bin explicitly
        if not path and os.path.exists(go_bin):
            potential_path = os.path.join(go_bin, tool)
            if os.path.exists(potential_path):
                path = potential_path
        
        if path is None:
            missing_tools.append(tool)
        else:
            # Check if it's the right version (ProjectDiscovery tools usually support -version)
            # If it's httpx, we want to be sure it's not the python one
            if tool == "httpx":
                try:
                    res = subprocess.run([path, "-version"], capture_output=True, text=True, timeout=2)
                    if "ProjectDiscovery" not in res.stdout and "ProjectDiscovery" not in res.stderr:
                        # If the one in PATH is wrong, check ~/go/bin specifically
                        if os.path.exists(os.path.join(go_bin, "httpx")):
                            path = os.path.join(go_bin, "httpx")
                        else:
                            print(f"[!] Warning: Found 'httpx' but it's not the ProjectDiscovery version.")
                except:
                    pass

    if missing_tools:
        print(f"[!] Warning: The following tools are missing: {', '.join(missing_tools)}")
        print("[!] Please use 'docs/cloudshell_setup.md' to install them.")
        return False
    
    print("[+] All required tools found. System is healthy!")
    return True
