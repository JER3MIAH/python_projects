class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('running')

player1 = PlayerCharacter('JOJOO')

print(player1.name)