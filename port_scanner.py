import socket

class PortScanner:
    def __init__(self, target,time_out=0.05,banner_timeout=2):
        # store the target IP here
        self.target_ip=target
        self.time_out=time_out
        self.banner_timeout=banner_timeout
        self.open_ports=[]

    def scan_port(self, port):
        
        # attempt connection to target:port
        # return True if open, False if closed
        with socket.socket() as s:
            s.settimeout(self.time_out)
            result=s.connect_ex((self.target_ip,port))
            

            return result==0

    def scan_range(self, start_port, end_port):
        # loop through ports start to end
        # call scan_port for each
        # print whether open or closed

        for i in range(start_port,end_port+1):
            val=self.scan_port(i)

            if val:
               
                print(f"Port {i} is Open")
                self.open_ports.append(i)
                banner=self.grab_banner(i)
                if banner:
                    print(f"Banner {banner}")

    def grab_banner(self, port):
        try:
            with socket.socket() as s:
                s.settimeout(self.banner_timeout)
                if s.connect_ex((self.target_ip,port)) == 0:
                    data = s.recv(1024)
                    return data.decode()
        except(socket.error, UnicodeDecodeError):
            return None
    


target = input("Enter target IP: ")
scanner = PortScanner(target)
scanner.scan_range(1, 1024)
print("----------END----------")