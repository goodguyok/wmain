from wmain.socket import Host
import time
import threading

if __name__ == '__main__':
    server = Host('127.0.0.1', 12012)
    server.accept()
    client = Host()
    client.connect('127.0.0.1', 12012)
    client.send('Hello, 12!'*5)
    client.send('cnm 12!')
    client.send('md, 12!')
    while 1:
        if server.has_msg():
            print([i[1] for i in server.recv_all()])
            break
        time.sleep(0.1)
    client.close()
    client.connect('127.0.0.1', 12012)
    client.send('Hello, 12!'*5)
    client.send('cnm 12ssasas傻逼吧!')
    client.send('md, 12!')
    
    while 1:
        client.send('md, 12!')
        if server.has_msg():
            print([i[1] for i in server.recv_all()])
            break
        time.sleep(0.1)
    server.close()
    server.stop_accept()
    print(threading.enumerate())
    print('Done.')