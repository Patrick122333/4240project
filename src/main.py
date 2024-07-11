import subprocess
import xml.etree.ElementTree as ET
import yaml

# Get the exploits that are defined in the exploits.yml file and set them as exploits
with open("exploits.yml", "r") as file:
    exploits = yaml.safe_load(file)["exploits"]

# Prompt user for the target IP address
target = input("Please Enter the target IP address: ")

# This runs the nmap command with the provided target IP address from the previous step
# -sV identifies the services running on the open ports while -oX allows for saves the scan results in an xml file
nmap_command = ["nmap", "-sV", "-oX", "nmap_output.xml", target]
subprocess.run(nmap_command)

# This will parse the xml file that nmap stored its results in
tree = ET.parse("nmap_output.xml")
root = tree.getroot()

# This function checks to see if there are any matches from the exploits.yml file and the xml file from nmap
def version_matches(service_version, exploit_version):
    return exploit_version in service_version if exploit_version else True

# This list stores the matched Services that are found
services = []

# Searches through each "host" element that is stored in the nmap xml output file
for host in root.findall("host"):

    # Searches through each "port" element that is stored in the nmap xml output file
    for port in host.findall("ports/port"):

        # Obtains the port information
        portID = port.get("portid")
        protocol = port.get("protocol")
        service = port.find("service")

        # Searches to see if the "service" element exists in the nmap xml output file
        if service is not None:

            # Obtains the service information that is running on the port
            serviceName = service.get("name", "")
            serviceVersion = service.get("product", "") + " " + service.get("version", "")
            
            # After everything is Obtained, we compare it to the information in the yaml file
            # If exploits are matched, we append it to the services list
            for exploit in exploits:
                if exploit["service"] == serviceName and version_matches(serviceVersion, exploit["version"]):
                    services.append((portID, protocol, serviceName, serviceVersion))

# Prints the information that what has been matched from the xml file and the yml file
if services:
    print("\nPorts, services, and versions that match exploits:")
    for portID, protocol, service, version in services:
        print(f"Port: {portID}/{protocol}, Service: {service}, Version: {version}")
else:
    print("No matching ports, services, and versions found.")

