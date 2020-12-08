#!/usr/bin/python3
from dearpygui import core, simple
from XSSFilterBypass.PayloadCrafter import PayloadCrafter


def craftPayload():
    payloadCrafter = PayloadCrafter()
    with simple.window("Payload Crafter"):
        core.add_text("Welcome to the payload crafter.")
        core.add_input_text("Select a host")
    


def main():
    with simple.window("Select what you want to do"):
        core.add_text("H3110 W0r1d!")
        core.add_button("Click me")
        core.add_input_text("string")
        core.add_slider_float("float")
    core.set_main_window_size(800, 800)
    core.start_dearpygui()   

if __name__ == '__main__':
    main()
