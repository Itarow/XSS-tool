from dearpygui import core,simple
from XSSFilterBypass.PayloadCrafter import *

class PayloadCrafterGUI: 
    def __init__(self):
        payloadCrafter = PayloadCrafter()
        with simple.window("Payload Crafter"):
            core.add_text("Welcome to the payload crafter.")
            core.add_input_text("Select a host", source="host")
            core.add_button("Set host")
            
    