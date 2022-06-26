import cgi
import paramiko
import time
from datetime import date

today = date.today()
form = cgi.FieldStorage()
ip = form.getvalue('ipaddress')
username = "root"
password = "umec@123"
cmd ="cat /etc/os-release && echo HostName: $HOSTNAME"
print("Status: 200 OK")
print("Content-type: text/html")
print()  # 列印一行空白行，用於分隔HTTP Header和正文


def getoutput(cmd):
    ssh=paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=password) 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    output = '<br>'.join(ssh_stdout.readlines())
    return(output)

print("systel os info:<br>")
print (f"<font color='green'> {getoutput(cmd)}</font>")

