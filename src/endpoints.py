class Endpoint:
    def __init__(self, name, url, method='GET', headers={}, body=None):
        self.url = url
        self.method = method if method is not None else 'GET'
        self.headers = headers or {}
        self.body = body
        self.name = name
 
       