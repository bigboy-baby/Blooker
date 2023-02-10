# Blooker

Trash blooket flooding module

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Blooker

```bash
pip install Blooker
```

## Usage

```python
from Blooker import bot

code = input("Game Code: ")
name = input("Name: ")
am = int(input("Amount: "))

for n in range(am):
    status = bot.join(code, name, "Angry Bot")
    if status == True:
        print("Joined Game")
    else:
        print("Failed to Join")
```

## Author
Biggie / bigboy-baby / bigboybigboi / biggie.wtf

## License
Shut
