import os
import sys
from pysnmp.hlapi import *
sys.path.append(r"C:\github\WebAutomation")
from md.ping import pinglist,pingcheck
from md.fast_ping import ping_ip
# print(sys.path)

print("Status: 200 OK")
print("Content-type: text/html")
print()  # 列印一行空白行，用於分隔HTTP Header和正文

#1.快速ping scan，並返回在線ip於pingpass_list中
# pingpass_list = ping_ip()
# print(pingpass_list)


#2. 取得ip範圍: pinglist(1,254) = 192.168.0.1~253
iplist = pinglist(1,253)
print(iplist)

#取得再在線ip
pingpass_list = pingcheck(iplist)
print(pingpass_list)

#進行snmp連線抓取系統對應mib資訊
def finddevices(ip):
    (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) = next (
             getCmd(SnmpEngine(),
                    CommunityData('public', mpModel=0),
                    UdpTransportTarget((ip, 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
                    # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)))                  
     )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int (errorIndex) -1][0] or '?'))
    else:
        for varBind in varBinds:
            # print(varBind)
            # print(' = '.join([x.prettyPrint() for x in varBind]))
            xval = (' = '.join([x.prettyPrint() for x in varBind]))
            xval = xval.replace("SNMPv2-MIB::sysDescr.0 = ", "")
            # xval = xval.replace("SNMPv2-MIB::sysName.0 = ", "")           
            xval = xval.split(",")
            return (xval[0])

# pingpass_list="192.168.0.5,192.168.0.86,192.168.0.7"
# pingpass_list=pingpass_list.split(",")

#建立表單
tval="<table border='1'><tr><td>IP Address</td><td>Model</td></tr>"
try:
    for ip in pingpass_list:
        version=finddevices(ip)
        # version=version.strip()
        ahref="http://192.168.0.2/showos.py?ipaddress="+ip
        tval=tval+"<tr><td><a href='"+ahref+"' target='_blank'>"+ip+"</a></td>"
        tval=tval+"<td>"+str(version)+"</td></tr>"
    tval = tval+"</table>"
    print(tval)
except:
    pass