# Socket Programming #
## Background info ##

**IP Address**: 32-bit IP addresses are used to identify nodes on the internet, i.e. used to identify *computers*.

For now we will use the simplifying assumption that each computer on the internet has a unique IP. This is not exactly true as IP addresses within different local networks can repeat. However nodes are still identified by a process based on unique IPs.

**Port Number**: one node can have multiple port numbers. Port numbers are used to identify *application processes* running on a node.

**Socket**: Software structure within a network node that serves as an endpoint for sending and recieving data across the network. It is created only during the lifetime of a process of an application running in the computer. The socket is defined by source IP and port numbers.

# Task 1: Client and server processes on the same computer #
This taks involved two steps: 
1. Run separate IDLE instances so that we can run more than one application process on our computer.
## Step 1 ##


