import threading
import subprocess
import time
from queue import Queue

# 定義工作執行緒
WORD_THREAD = 50

# 將需要 ping 的 ip 加入佇列
IP_QUEUE = Queue() 
for i in range(1,255):
    IP_QUEUE.put('192.168.0.'+str(i))

pingpass_list =[]

# 定義一個執行 ping 的函式
def ping_ip():
    global pingpass_list 
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        res = subprocess.call('ping -n 2 -w 5 %s' % ip,stdout=subprocess.PIPE)  # linux 系統將 '-n' 替換成 '-c'
        # 列印執行結果
        # print(ip,True if res == 0 else False)
        if res == 0:
            pingpass_list.append(ip)
    return pingpass_list

if __name__ == '__main__':
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_ip)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('程式執行耗時：%s' % (time.time() - start_time))
    print(f"在線的IP:{pingpass_list}")

    with open('pingpass.txt', 'w') as f:
        for ip in pingpass_list:
            f.write("%s\n" % ip)