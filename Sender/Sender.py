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
        fields = fields.split('&')
        for field in fields:
            field = field.split('=')[0]
        self.fields = data
        
    def craftData(self):
        crafted = []
        if self.field in self.fields:        
            fields = self.fields.split('&')
            for idx, field in enumerate(fields):
                field = field.split('=')[0]
                if self.field == field:
                    field = field + payload
                if idx != len(fields) - 1:
                    crafted.append(field)
            crafted = '&'.join(crafted)
        else:
            sys.stderr.write("Error. vulnerable field has to be in data.")
            raise ValueError
        return crafted
                        
    def send(self, payload):
        r = requests.post(self.url, craftData(payload))
        print(r.text)
        
        if payload in r.text:
            print("[~] Injection réussie")
        else
            print("[~] Injection ratée")

        
        