from . import request

class Test_injection():
    sql_injection_mod = 'sqli'
    shell_injection_mod = 'shelli'
    def __init__(self,injection_mod,injection_list,inject_url,tests_numbers:int=None,func=lambda u:u,timeout=20,method='GET'):
        if not tests_numbers:
            tests_numbers = len(injection_list)
        self.scan = {"i_m":inject_mod,"i_l":injection_list,"i_u":inject_url,'t_n':tests_numbers,'func':func,'method':method}
        self.out = {}
        self.timeout = timeout
    def _replace(self,url,id):
        return url.replace('$target',id)
    
    def test(self):
        for i in range(self.scan['t_n']):
            #Not Compileted
            new = request.Request(self.scan['i_u'],self.scan['method'])
            res = new.GetResponse()
            out = new.GetText()
            new.close()
            