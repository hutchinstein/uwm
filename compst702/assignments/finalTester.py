class Player:
    """Player Class.  First name and last name are input by user for new players.
    All new players default wins, losses and purse is set to 0"""
    def __init__(self, f_name, l_name, wins, losses, purse):
        self.f_name = f_name
        self.l_name = l_name
        self.wins = wins
        self.losses = losses
        self.purse = purse

a = open("players.txt", "r")

counter = 1
print("Select your player:")
for i in a:
    print(str(counter) + ".", i.strip().split(',')[0])
    counter += 1
print(str(counter) + ". New Player")
player = int(input("Enter your selection: "))
a.close()

a = open("players.txt", "r")
counter = 1
myPlayer = ''
for i in a:
    if counter == player:
        fname = i.strip().split(',')[0]
        lname = i.strip().split(',')[1]
        wins = i.strip().split(',')[2]
        losses = i.strip().split(',')[3]
        purse = i.strip().split(',')[4]
    counter += 1
a.close()

player = Player(fname, lname, wins, losses, purse)
print(player.f_name + player.l_name)
# print(playerInfo)
# a.readline()
# name = a.readline().split(",")[0]
# print("name", name)
