from bard import AskBard
import argparse
API_TOKEN = '<TOKEN>'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Parse arguments")
    parser.add_argument('-p', '--prompt')
    args = parser.parse_args()
    bard = AskBard(api_key = API_TOKEN)
    if args.prompt:
        response = bard.ask(args.prompt)
        print("Bard: ", response, end = "\n\n")
    while True:
        prompt = input("Enter a prompt here: ")
        if prompt == "quit":
            break
        response = bard.ask(prompt)
        print("Bard: ", response, end = "\n\n")
