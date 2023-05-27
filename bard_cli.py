"""Module providingFunction for CLI."""

import argparse
from enum import Enum
from bard import AskBard
API_TOKEN = '<TOKEN>'


class ColorCodes(Enum):
    """Represent color codes for setting string colors"""
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Parse arguments")
    parser.add_argument('-p', '--prompt')
    args = parser.parse_args()
    bard = AskBard(api_key = API_TOKEN)
    if args.prompt:
        response = bard.ask(args.prompt)
        print(ColorCodes.BOLD.value + ColorCodes.OKCYAN.value + "Bard: "
              + ColorCodes.ENDC.value, response, end = "\n\n")
    while True:
        prompt = input(ColorCodes.BOLD.value
                       + ColorCodes.OKGREEN.value + "Enter a prompt here: " + ColorCodes.ENDC.value)
        if prompt == "quit":
            break
        response = bard.ask(prompt)
        print(ColorCodes.BOLD.value + ColorCodes.OKCYAN.value + "Bard: ", response, end = "\n\n")
