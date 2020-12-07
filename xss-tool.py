#!/usr/bin/python3
from dearpygui import core, simple


def main():
    with simple.window("h4x0r"):
        core.add_text("H3110 W0r1d!")
        core.add_input_text("string")
        core.add_slider_float("float")
    core.start_dearpygui()    



if __name__ == '__main__':
    main()
