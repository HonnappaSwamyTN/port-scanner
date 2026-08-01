import socket
from concurrent.futures import ThreadPoolExecutor
import threading

class PortScanner:
    def __init__(self, target,time_out=0.05,banner_timeout=2):
        # store the target IP here
        self.target_ip=target
        self.time_out=time_out
        self.banner_timeout=banner_timeout
        self.open_ports=[]
        self.lock=threading.Lock()

    def scan_port(self, port):
        
        # attempt connection to target:port
        # return True if open, False if close
        s=socket.socket()
        s.settimeout(self.time_out)
        result=s.connect_ex((self.target_ip,port))

        if result == 0:
            return s
        else:
            s.close()
            return None
    
    def single_port_processor(self, port):
        val=self.scan_port(port)
        if val:
            try:
                try:
                    serv=socket.getservbyport(port)
                except (OSError,OverflowError):
                    serv="Unknown service"
                
                banner=self.grab_banner(port,val)
                if banner:
                    print(f"Banner {banner}")
                
                with self.lock:
                    self.open_ports.append(port)
                    
                print(f"port : {port},Service : {serv}")
            
            finally:
                val.close()


    def scan_range(self, start_port, end_port):
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.single_port_processor,range(start_port,end_port+1))

    def grab_banner(self, port, sock):
        try:
            sock.settimeout(self.banner_timeout)
            http_ports = [80, 443, 8080, 8443]
            if port in http_ports:
                sock.send(("GET / HTTP/1.1\r\nHost: " + self.target_ip + "\r\n\r\n").encode("utf-8"))
            data = sock.recv(1024)
            return data.decode()
        except(socket.error, UnicodeDecodeError):
            return None
    


target = input("Enter target IP: ")
scanner = PortScanner(target, time_out=1)
scanner.scan_range(1, 1024)
print("----------END----------")