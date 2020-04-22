import time
from datetime import datetime as dt
hosts_path="/etc/hosts"
hosts_temp="/Users/gopalkrishnashukla/eclipse-workspace/Project3/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.facebook.com","https://www12.gogoanime.io/","https://www.crunchyroll.com/en-gb","https://www.chess.com/home"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours")
    time.sleep(5)
