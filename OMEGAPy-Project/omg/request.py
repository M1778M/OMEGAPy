class Request():
    def __init__(self,url:str,method:str,params={},data={},headers={},timeout=int(200),auth=()):
        import httpx
        self.url = url
        self.method = method
        self.params = params if params else {}
        self.data = data if data else {}
        self.headers = headers if headers else {}
        self.auth = auth if auth else ()
        self.timeout = timeout if timeout else 1000
        self.Respose = httpx.request(url=self.url,method=self.method,params=self.params,data=self.data,headers=self.headers,auth=auth,timeout=timeout)
    def GetText(self):
        return self.Response.text
    def GetResponse(self):
        return self.Respose.status_code
    def GetHeaders(self):
        return self.Respose.headers
    def GetRequest(self):
        return self.Respose.request
    def GetURL(self):
        return self.Respose.url
    def Close(self):
        return self.Respose.close()
    def IsClosed(self):
        return self.Respose.is_closed
    def GetHistoty(self):
        return self.Respose.history


class r:
    def __init__(self):
        pass
    @classmethod
    def get(url:str,params:{},data:{},headers:{},auth:(),timeout:int(20)):
        method = 'get'
        return Request(url=url,method=method,params=params if params else {},data=data if data else {},headers=headers if headers else {},auth=auth if auth else (),timeout=timeout if timeout else 1000)
    @classmethod
    def post(url:str,params:{},data:{},headers:{},auth:(),timeout:int(20)):
        method = 'post'
        return Request(url=url, method=method, params=params if params else {}, data=data if data else {},
                       headers=headers if headers else {}, auth=auth if auth else (),
                       timeout=timeout if timeout else 1000)
    @classmethod
    def put(url:str,params:{},data:{},headers:{},auth:(),timeout:int(20)):
        method = 'put'
        return Request(url=url, method=method, params=params if params else {}, data=data if data else {},
                       headers=headers if headers else {}, auth=auth if auth else (),
                       timeout=timeout if timeout else 1000)
