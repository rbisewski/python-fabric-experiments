#!/usr/bin/python3

import sys, getopt, getpass
from fabric import Connection

def main(argv):

    usageInfo = "check-kernel.py -d <destination hostname or IP> -p <port number> -u <user> -i </path/to/identity_file>"

    destinationHost = ''
    destinationPort = 22 
    user = ''
    identityFile = ''
    
    #
    # input validation
    #
    
    try:
        opts, args = getopt.getopt(argv,"hd:p:u:i:",["host=","port=","user=","id="])
    except getopt.GetoptError:
        print(usageInfo)
        exit(1)
    
    for opt, arg in opts:
        if opt == "-h":
            print(usageInfo)
            exit()
        elif opt in ("-d","--host"):
            destinationHost = arg
        elif opt in ("-p","--port"):
            destinationPort = arg
        elif opt in ("-u","--user"):
            user = arg
        elif opt in ("-i","--id"):
            identityFile = arg
    
    if destinationHost == '':
        print("Error: No host specified.")
        exit(1)
    
    if destinationPort == 0 or not destinationPort.isdigit():
        print("Error: Invalid port specified.")
        exit(1)
    
    if user == '':
        print("Error: No user specified.")
        exit(1)

    #
    # if an identity is supplied, attempt to obtain the passphrase
    #
    identityPassphrase = getpass.getpass()
    
    #
    # attempt to connect using the given parameters
    #
    
    if identityFile == '' or identityPassphrase == '':
        conn = Connection(host=destinationHost, port=destinationPort, user=user)
    else:
        conn = Connection(host=destinationHost, port=destinationPort, user=user,
          connect_kwargs={'key_filename':identityFile,'passphrase':identityPassphrase})
    
    if conn is None:
        print("Error: Unable to initialize Connection object.")
        exit(1)
    
    print("The following connection was established: ", conn)

    # this will attempt to obtain the kernel information and print it to
    # stdout, and then close the connection
    result = conn.run("uname -a")

    if result.exited != 0 or result.ok != True:
        print("Warning: The connection was improper or terminated prematurely.")

    conn.close()

#
# execute the main function declared above
#
main(sys.argv[1:])
