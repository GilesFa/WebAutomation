import cgi
import paramiko
import time
from datetime import date

today = date.today()
form = cgi.FieldStorage()
ip = form.getvalue('ip')
# username = form.getvalue('username')
# password = form.getvalue('password')
username = "root"
password = "umec@123"
cmd = form.getvalue('cmd')
grep = form.getvalue('grep')

#當grep欄位為空值時
if grep == None:
    ssh_cmd = cmd
else:
    ssh_cmd = cmd + "|grep " + grep

print("Status: 200 OK")
print("Content-type: text/html")
print()  # 列印一行空白行，用於分隔HTTP Header和正文
print(f"<h2>Today: {today}</h2>")
print(f"<h2>Remote server ip: {ip}</h2>")
print(f"<h2>You type cmd: <font color='red'><b>{ssh_cmd}</b></font></h>")


def getoutput(cmd):
    ssh=paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=password) 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
    output = '<br>'.join(ssh_stdout.readlines())
    return(output)

print("<h3>output:<br>")
print (f"<font color='green'> {getoutput(cmd)}</font><h4>")

