from dcgsasklist.AskException import AskException

class Ask:

    def __init__(self, list: list):
        self.list = list

    def ask(self, question = ""):
        position = 1
        for option in self.list:
            print(str(position) + " - " + option)
            position += 1
        user_response = input(question + " ")
        try:
            return self.list[int(user_response) - 1]
        except IndexError:
            raise AskException("You The choosed option is not part from the set presnted.")
            
