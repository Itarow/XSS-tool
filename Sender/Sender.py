import requests
import sys


class Sender:
    def __init__(self, **kwargs):
        self.url     = kwargs["url"]
        self.fields  = kwargs["data"] 
        self.payload = kwargs["payload"]
        self.field   = kwargs["field"]
        try:
            self.cookie = kwargs["cookie"]
        except KeyError:
            pass
        try:
            self.headers = kwargs["headers"]
        except KeyError:
            pass
        
    def setFields(self, fields):
        self.fields = fields
        
    def craftData(self):
        crafted = []
        if self.field in self.fields:        
            fields = self.fields.split('&')
            for field in enumerate(fields):
                if self.field==field:
                    field = field.split('=')[0]
                    field = field + payload
                    crafted.append(field)
            crafted = '&'.join(crafted)
        else:
            sys.stderr.write("Error. vulnerable field has to be in data.")
            raise ValueError
        return crafted
                        
    def send(self, payload):
        try:
            r = requests.post(self.url, craftData(payload))
            print(r.text)
            print("[~] Injection succeed, get on the page to see the result")
        except:
            print("[~] Error.")
        
        