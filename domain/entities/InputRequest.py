class InputRequest:

    def __init__(self):
        self.params = None
        self.headers = None
        self.data = None
        self.verify=None
        self.json=None
        self.path=None
        self.timeout=None
        self.files = None
        self.cert= None
        self.asyncc= None

    def setMethod(self, method):
        self.method = method
        return self
    
    def setPath(self, path):
        self.path = path
        return self
    
    def setHeaders(self, headers):
        self.headers = headers
        return self
    
    def setParams(self, params):
        self.params = params
        return self
    
    def setData(self, data):
        self.data = data
        return self
    
    def setVerify(self, verify):
        # You can pass verify the path to a CA_BUNDLE file or directory with certificates of trusted CAs:
        # verifica ca del server al cual le pego.
        self.verify = verify
        return self
    
    def setTimeOut(self, timeout):
        self.timeout = timeout
        return self
    
    def setFile(self, files):
        #files=files
        self.files = files
        return self
    
    def setCert(self, cert):
        #requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
        self.cert = cert
        return self
    
    def setJson(self, json):
        self.json = json
        return self
    
    def setAsyncc(self, asyncc):
        self.asyncc = asyncc
        return self
   

