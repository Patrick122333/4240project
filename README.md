# 4240project

## Description:
This project is to show a few examples of system penetration. I will be using two virtual machines (both running Ubuntu linux version 22.04) with one running the Metasploitable 2 test environment (https://sourceforge.net/projects/metasploitable/). I have included four python scripts to explore four of the vulnerabilities present on the test environment. I have also included a simple payload file that serve to retrieve wanted data post exploitation. 

When presenting these examples I will be going through these steps
- network scanning
- vulnerbility assessment
- exploitation
- post-exploitation

## Purpose:
The purpose of the project is to show how vulnerable many systems are and to highlight how unexpected some of these vulnerabilities can be. After the reviewing the examples shown, the user should understand the importance of maintaining software updates, the importance of a SOC team for an organization, and the need to strictly follow cyber security best practices in order to ensure both system security and system integrity. 

## Requirements:
- Metasploitable 2
- Virtualbox 
-

## Exploits/Vulnerabilities:

### SAMBA CVE-2007-2447 PORT 445 VERSIONS <>= 3.0.25rc3
- Samba is a software that is a re-implmentation of the SMB networking protocol. This software provides file and print services for all clients as long as they are using the SMB protocol.
- This exploit takes advantage of an 

### UnrealRCD CVE-2010-2075 PORT 6667 VERSION 3.2.8.1 
- UnrealRCD is a daemon for Internet Realy Chat usage in order to provide chat services.
- This exploit

### VSFTP CVE-2011-2523 PORT 21 VERSION 2.3.4
- Vsftp is an ftp server
- 

### SSH WEAK PASSWORD (BRUTE FORCE EXAMPLE)
- SSH is used to remotely connect to another system over a network. 
- There is no issue with the SSH software itself, but there is with the weak passwords that were set (and lack of configuration to ensure that the individual connecting is an authorized one.)

## Payload:
-

# Guide To Test:
