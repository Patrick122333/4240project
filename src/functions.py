#functions for pentesting specific exploits presented
#in metasploitable 2

import subprocess

def run_nmap(ip_addr):
    try:
        # Example command: nmap -sP <ip_address>
        cmd = ["nmap", "-sP", ip_addr]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Nmap command failed: {e}"
