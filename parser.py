from xml.dom import minidom 

import os.path
def nmapit():
    nmapstyle = {
            "type": str,
            "port": int,
            "status": {
                "state": str,
                "response" :str 
                },
            "service": {
                "name": str 
                }
    }
    return nmapstyle

def parser(xmlfile):
    nmapitem = []
    items = loc.getElementsByTagName('port')
    j=0
    for i in items: 
        nmapitem.append(nmapit())
        nmapitem[j]["type"] = i.attributes.items()[0][1]
        nmapitem[j]["port"] = i.attributes.items()[1][1]
        
     #   print(i.attributes.items()[0][1] + " - " + i.attributes.items()[1][1])
        
        for k in i.getElementsByTagName('state'):

            nmapitem[j]["status"]["state"] = k.attributes.items()[0][1]
            nmapitem[j]["status"]["response"] = k.attributes.items()[1][1]
            
         #   print(k.attributes.items()[0][1] + " - " + k.attributes.items()[1][1])
        
        if(i.getElementsByTagName('service')):
            for k in i.getElementsByTagName('service'):
                nmapitem[j]["service"]["name"] = k.attributes.items()[0][1]
             #   print(k.attributes.items()[0][1] + "\n")
        else:
            nmapitem[j]["status"]["name"] = "Service Not Found"
           # print("Service not found\n")
        j +=1
    return nmapitem

loc = minidom.parse('here.xml')
x = parser(loc)
for i in range(len(x)):
    print(x[i])