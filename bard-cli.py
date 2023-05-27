from bard import AskBard
import argparse
API_TOKEN = '<TOKEN>'


class bcolors:
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
        print(bcolors.BOLD + bcolors.OKCYAN + "Bard: " + bcolors.ENDC, response, end = "\n\n")
    while True:
        prompt = input(bcolors.BOLD + bcolors.OKGREEN + "Enter a prompt here: " + bcolors.ENDC)
        if prompt == "quit":
            break
        response = bard.ask(prompt)
        print(bcolors.BOLD + bcolors.OKCYAN + "Bard: ", response, end = "\n\n")
