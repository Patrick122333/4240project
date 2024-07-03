import subprocess

def run_nmap(ip_addr):
    try:
        # Example command: nmap -sP <ip_address>
        cmd = ["nmap", "-sP", ip_addr]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Nmap command failed: {e}"

def main():
    # Prompt the user for an IP address
    ip_addr = input("Enter the IP address to scan with Nmap: ")
    
    # Run the nmap function
    result = run_nmap(ip_addr)
    
    # Display the result
    print("Nmap Scan Results:")
    print(result)

if __name__ == '__main__':
    main()