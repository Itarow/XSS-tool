import requests
import sys
from Sender.Sender import Sender


class Check:
    def check_htmlentities(self, url, xssurl=None, **fields):
        regular_payload = '<script>alert(1337)</script>'
        
        #Give random value to all fields.
        # @TODO give the ability to use special values (ex: emails, passwords > 8 letters...)
        for field in fields:
            fields[field] = "random_value"
            
        if xssurl == None:
            for field in fields:
                fields[field] = regular_payload

                r = requests.post(url, data=fields)
                if regular_payload not in r.text:
                    if '&lt' in r.text:
                        print(f'[~] It seems that the website is using html entities.')
                    else:
                        print(f'[~] There might be a filter on the input or the field {field} might not be vulnerable to XSS.')
                else:
                    print(f'[~] The website might be vulnerable to XSS on the field: {field}')
                fields[field] = 'random_value'
        else:
            for field in fields:
                fields[field] = regular_payload
                
                sess = requests.Session()
                r = sess.post(url, data=fields)
                r = sess.get(xssurl)
                if regular_payload not in r.text:
                    if '&lt' in r.text:
                        print(f'[~] It seems that the website is usint html entities.')
                    else:
                        print(f'[~] There might be a filter on the input or the field {field} might not be vulnerable to XSS.')
                else:
                    print(f'[~] The website might be vulnerable to XSS on the field: {field]')

