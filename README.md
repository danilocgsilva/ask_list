# Ask_list
Api that consumes a list and asks to user givin him a number to choose

## Installing

1. Go to the root project directory
2. Type:
```
pip install .
```
3. Done!

## Using
```
from dcgsasklist.Ask import Ask

list_options = [
    "Sun",
    "Sirius",
    "Betegueuse",
    "Brachium"
]

ask = Ask(list_options)

response = ask.ask("Choose one:")

print("The response is " + response)
```
