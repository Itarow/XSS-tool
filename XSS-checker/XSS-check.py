import requests
import sys
from Sender.Sender import Sender


class Check:
    sender = Sender(url=url, data=data, field=field)
    sender.setField("comment")
    sender.send(payload)