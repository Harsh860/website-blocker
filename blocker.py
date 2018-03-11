import time
from datetime import datetime as dt 
redirect="127.0.0.1"
hosts_path="/etc/hosts"
websites=["facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13) :
        print("work \n")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else :
                    file.write(redirect+" "+ website+"\n")
            print(content)

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites ):
                    file.write(line)
            
            file.truncate()
            print(content)



    time.sleep(5)


