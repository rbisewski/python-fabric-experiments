# python-fabric-experiments

Compilation of various simple python fabric scripts. Primarily the goal is
to include code that can make managing clusters more efficient. At this
time not much code is present here.

## check-kernel.py

Conduct a quick lookup of the kernel version and type of a given Linux host.

## print-var-log.py

Prints the files and their sizes, in the /var/log/ directory of a given
Linux host.

## check-zpool.py

Prints the health status of the zpool on a given host, as well as the ZFS
volume information.

## TODO

* consider separating out parts into separate functions
* add a script to handle log rotation and perhaps log partition cleanup
