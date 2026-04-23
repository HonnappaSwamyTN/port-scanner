import socket

class PortScanner:
    def __init__(self, target,time_out=0.05):
        # store the target IP here
        self.target_ip=target
        self.time_out=time_out

    def scan_port(self, port):
        
        # attempt connection to target:port
        with socket.socket() as s:
            s.settimeout(self.time_out)
            result=s.connect_ex((self.target_ip,port))
            

            return result==0
        # return True if open, False if closed

    def scan_range(self, start_port, end_port):

        for i in range(start_port,end_port+1):
            val=self.scan_port(i)

            if val:
                print(f"Port {i} is Open")
            else:
                print(f"Port {i} is closed")

        # loop through ports start to end
        # call scan_port for each
        # print whether open or closed

target = input("Enter target IP: ")
scanner = PortScanner(target)
scanner.scan_range(1, 1024)