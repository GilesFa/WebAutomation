import os

def pinglist(x,y):
    global ip_list
    ip_list = []
    for i in range(0,x):
        for j in range(1,y):
            # print(f"192.168.{i}.{x}")
            ip = f"192.168.{i}.{j}"
            ip_list.append(ip)
    return ip_list
if __name__ == "__main__":
    pinglist(1,6)
    print(ip_list)


def pingcheck(ip):
    global pingpass_list
    pingpass_list = []
    for ip in ip_list:
        # print(ip)
        response = os.popen(f"ping {ip} -n 2 -w 5").read()
        if "已遺失 = 0" in response:
            # print(f"UP {ip} Ping Successful")
            pingpass_list.append(ip)
        else:
            pass
            # print(f"DOWN {ip} Ping Unsuccessful")
    return pingpass_list
    # print(pingpass_list)
if __name__ == "__main__":
    pingcheck(ip_list)
    print(pingpass_list)
