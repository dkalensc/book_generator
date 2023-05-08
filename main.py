#!/usr/bin/env python3
from generators import story_generator as sg
"""
This is the main entry point for the Book Generator App
"""

__author__ = "Daniel Kalenshcer"
__version__ = "0.1.0"
__license__ = "N/A"


def main():
    """ Main entry point of the app """
    print("Book Generator Start")
    generator = sg.StoryGenerator()
    generator.generate_story()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()