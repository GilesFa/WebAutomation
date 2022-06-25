from pysnmp.hlapi import *

print("Status: 200 OK")
print("Content-type: text/html")
print()  # 列印一行空白行，用於分隔HTTP Header和正文


from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public', mpModel=0),
                          UdpTransportTarget(('192.168.0.5', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))):
    if errorIndication or errorStatus:
        print(errorIndication or errorStatus)
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))