import requests
import sys
from time import sleep


def main():
    print("Input a target URL")
    url = input("Input your targeted url: ")

    initiate_scanning = "URL Scanning In Progress...\n"
    for i in initiate_scanning:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.1)
    file = open("possible_admin_panels.txt", "r") #file that ontain a list of possible admin panel repos
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print("*" * 15)
                print("An Admin Panel has been detected ==> {}".format(curl))
                print("*" * 15)
            else:
                print("[No Admin Panel Detected".format(curl))
    except KeyboardInterrupt:
        print("Programm Interrupted by user")
    except:
        print("Unknown Error")
    file.close()


if __name__ == "__main__":
    main()
#Written By Joel Greyhat
#AP_Recon v1.0
