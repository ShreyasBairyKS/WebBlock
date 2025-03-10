import time
from datetime import datetime as df

status = False # starts and stops the blocker depedding on the button pressed
port = '127.0.0.1'
host_path = 'C:\Windows\System32\drivers\etc\hosts'
#print(host_path)
#host_path = r'host.txt'
websites = []

with open("websites.txt", "r+") as file:
    websites = file.read().split("\n")[:-1]

def blocker(start_time, stop_time):
    """
    checks if the current time is within the start_time and stop_time is,
    if the current time is within thestart and stop time, then it adds the websites from websites.txt to the hosts file to
    and if the current time is not within the start time and stop time, it then removes the websites from the hosts file
    """
    while status:
        if df(df.now().year, df.now().month, df.now().day, start_time) < df.now() < df(df.now().year, df.now().month, df.now().day, stop_time):
            print('work now')
            with open(host_path, "r+") as host:
                content = host.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        host.write('\n' + port + ' ' + website)
            
        else:
            print('non work time')
            with open(host_path, "r+") as host:
                content = host.readlines()
                host.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        host.write(line)
                host.truncate()
        time.sleep(5.0)
    else:
        with open(host_path, "r+") as host:
                content = host.readlines()
                host.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        host.write(line)
                host.truncate()

