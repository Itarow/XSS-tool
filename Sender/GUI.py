from dearpygui import core,simple
from Sender import Sender

class SenderGUI: 
    def __init__(self):
        with simple.window("Sender"):
            core.add_text("Welcome to the payload crafter.")
            core.add_input_text("Select a host", source="host")
            core.add_input_text("Select a target", source="target")
            core.add_input_text("Set data", source="data")
            core.add_input_text("Set vulnerable field", source="field")
            core.add_input_text("Set payload", source="payload")            
            
            core.add_button("Send", callback=self.send)
            
    def send(self, *args):
        pass