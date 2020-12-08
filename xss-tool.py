#!/usr/bin/python3
import argparse

from dearpygui import core, simple

from XSSFilterBypass.PayloadCrafter import PayloadCrafter


def usage():
    print("Usage of xss-tool:")
    print("-h, --help          : show this message and exit")
    print("-i, --interactive   : interactive xss-tool shell")
    print("-g, --gui           : interactive gui")

def main():
    usage()   

if __name__ == '__main__':
    main()
