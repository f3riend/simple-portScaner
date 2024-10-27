from icecream import ic
import threading
import socket



localhost = '127.0.0.1'
startPort = 1
endPort = 1024


def portScanner(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((localhost, port))

        if result == 0:
            ic(f"Port {port} is open") # you can use print also
        else:
            pass


threads = []
for port in range(startPort, endPort + 1):
    t = threading.Thread(target=portScanner, args=(port,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()
