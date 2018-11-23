from socket import *
import sys,os,re
from dnslib import *

class bl:
    def __init__(self,Info):
        self.name=Info[:len(Info)-2]
        self.errcode=Info[len(Info)-1]

f = open('dnsproxy.cfg')
cfg = [re.sub('^|\n|', '',i) for i in f]

dnssrv = cfg[1]
BL=cfg[3:]
BL=[bl(i) for i in BL]
print "Black List is"
for i in BL:
    print i.name,'  ',i.errcode


port = 53
addrs = ('10.44.253.9',port)
addrc = (dnssrv,port)
srv_socket = socket.socket(AF_INET, SOCK_DGRAM)

client_socket = socket.socket(AF_INET, SOCK_DGRAM)

srv_socket.bind(addrs)




while True:
        conns, addr = srv_socket.recvfrom(1024)

        d = DNSRecord.parse(conns)
        name = d.questions[0].get_qname().idna()[:len(d.questions[0].get_qname().idna())-1]
        print addr,' => ',name

        comp = [i for i in BL if i.name==name]
        if len (comp)>0:
            print comp[0].name,' failure code ',comp[0].errcode
            d = DNSRecord(DNSHeader(qr=1,aa=1,ra=1),q=DNSQuestion(name))

            d.header.rcode=int(comp[0].errcode)

            conns = DNSRecord.pack(d)

            srv_socket.sendto(conns,addr)

        else:
            client_socket.sendto(conns,addrc)
            connc, addrdns = client_socket.recvfrom(1024)

            srv_socket.sendto(connc,addr)



