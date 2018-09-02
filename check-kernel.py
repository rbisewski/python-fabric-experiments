#!/usr/bin/python3

import sys, getopt
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
        opts, args = getopt.getopt(argv,"hd:p:u:",["host=","port=","user=","id="])
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
    # attempt to connect using the given parameters
    #
    
    conn = Connection(host=destinationHost, 
    port=destinationPort, 
    user=user, 
    connect_kwargs={'key_filename':identityFile})
    
    if conn is None:
        print("Error: Unable to initialize Connection object.")
        exit(1)
    
    print("The following connection was established: ", conn)

    # TODO: add code here to actually execute the commands on the remote
    #       server and gage the response...

#
# execute the main function declared above
#
main(sys.argv[1:])
