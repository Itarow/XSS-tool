#!/usr/bin/python3
from dearpygui import core, simple
from XSSFilterBypass.PayloadCrafter import PayloadCrafter
from XSSFilterBypass.GUI import PayloadCrafterGUI
from Sender import GUI
        
def summonPCGUI(sender, data):
    pcGUI = PayloadCrafterGUI()
        
def summonSenderGUI(sender, data):
    senderGUI = GUI.SenderGUI()
        
def main():
    with simple.window("Select what you want to do"):
        core.add_text("H3110 W0r1d!")
        core.add_button("Craft Payloads", callback=summonPCGUI)
        core.add_button("Send Payload", callback=summonSenderGUI)
    core.set_main_window_size(800, 800)
    core.start_dearpygui()   

if __name__ == '__main__':
    main()
