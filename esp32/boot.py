from wifi_connect import connect_wifi
from sd_connect import sd_connect

def main():
    try:
        connect_wifi()
        sd_connect()
    except Exception as err:
        print(err)

