#!/usr/bin/python3

import sys, getopt, getpass
from fabric import Connection

def main(argv):

    usageInfo = ("check-ceph-health.py "
                 "-d <destination hostname or IP>")

    destinationHost = ''
    destinationPort = 22 
    user = 'ceph-deploy-blade'
    
    #
    # input validation
    #
    
    try:
        opts, args = getopt.getopt(argv,"hd:p:u:i:",["host=","port=","user="])
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
    conn = Connection(host=destinationHost, port=destinationPort, user=user)
    
    if conn is None:
        print("Error: Unable to initialize Connection object.")
        exit(1)
    
    print("The following connection was established: ", conn)

    #
    # obtain the status of the ceph health / status information
    #

    result = conn.run("sudo ceph status")
    if result.exited != 0 or result.ok != True:
        print("Warning: The connection was improper or terminated prematurely.")
        print("Unable to obtain ceph cluster health status.")

    #
    # close the connection since everything is done
    #

    conn.close()

#
# execute the main function declared above
#
main(sys.argv[1:])
