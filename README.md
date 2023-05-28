#### Bard-CLI
This project currently is a python adapter that mainly uses the bard API python package [Bard-API](https://github.com/dsdanielpark/Bard-API) to have Command Line Interface (CLI) based interaction to Google's BARD. 

##### Note: Please review the instructions mentiond in the [Bard-API](https://github.com/dsdanielpark/Bard-API) for additional information and risks.

#### Pre-requistes
1. Install the necessary modules from requirements.txt 
```
pip install -r requirements.txt
```
2. Set up api token **TOKEN** in bard_cli.py. You can refer [Bard-API](https://github.com/dsdanielpark/Bard-API) project on how to get your **__Secure-1PSID** token

#### How to use it?
This will start of an interactive CLI with BARD 

```
python bard_cli.py
```

OR

This will start of an interactive CLI with BARD, where the first prompt given will be as mentioned in PROMPT 

```
python bard_cli.py -p "<PROMPT>"
```

#### How to quit the session?
You can quit the interactive cli session, by mentioning the keyword - **quit**

```
python bard-cli.py 

Enter a prompt here: hello

Bard:  Hello! How can I help you today?

Enter a prompt here: quit
```

#### Intersting way to invoke BARD-CLI instanly
Have a bash wrapper function like the given below added to you shell profile (like **bash_profile**), to avoid calling python intrepreter to invoke BARD-CLI
```
ask_bard() { python bard-cli.py -p "$1";}
```

You can then invoke the BARD-CLI anywhere in you terminal or shell like the below
```
ask_bard "Hows the weather today in London?"
```

