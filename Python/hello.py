import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()
name = form.getvalue('name')

print("Status: 200 OK")
print("Content-type: text/html")
print()  # 列印一行空白行，用於分隔HTTP Header和正文
print("<h1>Hello World! THis python </h1>")
print("<h2><font color='red'> <b>HaHa</b></font></h2>")
print(f"You name is {name}")
# import paramiko 
# import time
# ssh=paramiko.SSHClient() 
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname="192.168.0.5", username="root", password="umec@123") 
# ssh_stdin, ssh_stdout, ssh_stderr=ssh.exec_command('ls -l')
# # print(ssh_stdout.readlines())
# print("---------output--------------")
# print(''.join(ssh_stdout.readlines()))

# print("Status: 200 OK")
# print("Content-type: text/html")
# print()  # 列印一行空白行，用於分隔HTTP Header和正文
# print("<h1>Hello World! This is python</h1>")


