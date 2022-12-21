from . import etu
from .secure import SignMethodMaker
import socket
from threading import Thread

class stds:
    omegapy_str = 'OMEGAPacket '

class Connection:
    def __init__(self,host:str,port:int):
        self.host=host
        self.port=port
        self.connection = socket.socket(2,1)
    def connect (self):
        self.connection.connect((self.host,self.port))
    def __getattr__(self,attr):
        return getattr (self.connection,attr)
    def __call__(self):
        return self.connection
    def send(self,bytes_):
        return self.connection.send(bytes_)
    def recv(self,size):
        return self.connection.recv(size)

def declean(string):
    for i in string:
        string=string.replace('<%newline%>','\n')
    return string

def clean(string):
    for i in string:
        string=string.replace('\n','<%newline%>')
    return string
def _sclean(string):
    for i in string:
        print(string)
        string=string.replace(' ','')
    return string
def _lclean(ls):
    for i in range(len(ls)):
        if ls[i]=='':
            del ls[i]
    return ls
class Format:
    def __init__(self,FormatSign:str,FormatFrom:int,FormatTo:int):
        self.fs = FormatSign
        self.ff = FormatFrom
        self.ft = FormatTo
    def check_format(self,inpt):
        return True if inpt[self.ff:self.ft]==self.fs else False
    def format (self,inpt):
        def fromstr(ls):
            o=''
            for i in ls:
                o+=i
            return o
        copy = inpt[self.ff:self.ft]
        inpt = list(inpt)
        inpt[self.ff:self.ft] = self.fs
        return fromstr(inpt[self.ff:self.ft]+list(copy)+inpt[self.ft:])
    
class Packet:
    options = {'target':None,'port':None,'data':None,'Accepted':['true','false']}
    imp     = ['target','port']
    def __init__(self,formater:Format):
        self.packet_options = {}
        self.formater = formater
        self.formats = formater.fs
        self.options = Packet.options
        self._imp = Packet.imp
    def set_target (self,target):
        self.packet_options['target'] = target
    def set_data (self,data):
        self.packet_options['data'] = data
    def set_port(self,port):
        self.packet_options['port'] = port
    def set_new (self,name,value):
        self.packet_options[str(name)] = str(value)
        return True
    def create_packet(self):
        pack = '\n'
        for i in self._imp:
            if i not in self.packet_options.keys():
                raise UnknownError (f"cannot find '{i}' option in packet options")
            pack+=  self.secure_name(_sclean(str(i))) + ' : ' + clean(str(self.packet_options[i]))+'\n'

        for i in list(self.packet_options):
            if i in self._imp:
                continue
            pack+= self.secure_name(_sclean(str(i))) + " : " + clean(str(self.packet_options[i]))+'\n'
        return self.formater.format(pack)
    def secure_name (self,name):
        al = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_'
        for i in name:
            if i not in al:
                return False
            
        return name
    def send_packet(self):
        self.last_con = Connection(self.packet_options['target'],int(self.packet_options['port']))
        self.last_con.connect()
        self.last_con.send(self.create_packet().encode())
        return True
    def packet_decode(self,packet):
        make = {}
        pk=packet.split('\n')
        _lclean(pk)
        for i in pk[1:]:
            make[_sclean(i[:i.find(':')])] = i[i.find(':')+2:]
        return make
SecSign  = SignMethodMaker ('securecon')

FastSign = SignMethodMaker ('quickcon')

FastFormat = Format('FCP.! ',0,len('FCP.! ')-1)

class FastConnect:
    def __init__(self,host,port):
        self._host = host
        self._port = port
        self.signer = FastSign
        self.first_data = 'Hello!'
        self.default_data = 'NULL'
        self._flag = 0
        self.pk = Packet(FastFormat)
        self.pk.set_port(port)
        self.pk.set_target(host)
    def reset(self):
        self.pk = Packet(FastFormat)
        self.pk.set_port(self._port)
        self.pk.set_target(self._host)
    def send_packet (self,data:str=None,**kwargs):
        for i in list(kwargs):
            self.pk.set_new(i,kwargs[i])
        if self._flag == 0 and data==None:
            self.pk.set_data(self.first_data)
            self.pk.send_packet()
            self.reset()
            self._flag += 1
        elif self._flag >= 1 and data==None:
            self.pk.set_data(self.default_data)
            self.pk.send_packet()
            self.reset()
            self._flag += 1
        elif data != None:
            self.pk.set_data(data)
            self.pk.send_packet()
            self.reset()
            self._flag += 1
        else:
            return False
        return True
    

def _test_server (port):
    def _client_getter (client):
        while True:
            x=client.recv(1024*1024)
            if x==b'':
                continue
            print (x.decode())
    s = socket.socket(2,1)
    s.bind(('0.0.0.0',port))
    s.listen(-1)
    while True:
        cl = s.accept()
        Thread(target=_client_getter,args=(cl[0],)).start()
        
class Server:...

class Request:...

