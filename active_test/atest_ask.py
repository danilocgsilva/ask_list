from dcgsasklist.Ask import Ask

list_options = [
    "Sun",
    "Sirius",
    "Betegueuse",
    "Brachium",
    "Antares",
    "Hamal",
    "Aldebaran"
]

ask = Ask(list_options)

response = ask.ask("Choose one:")

print("The response is " + response)
