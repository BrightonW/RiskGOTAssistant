#RiskApp

CONST_ESSOS_TERR = 12
class Territory:
    def __init__(self, name: str, castle: bool, region) -> None:
        self.name = name
        self.castle = castle
        self.region = region
class Region:
    def __init__(self, name: str, rpower: int, terr: int) -> None:
        self.name = name
        self.rpower = rpower
        self.terr = terr

terr_data = []
complete_region = []
power = 0

# Define territories and regions using dictionaries
territories = {
    # Disputed Lands
    "lys": Territory("Lys", False, "The Disputed Lands"),
    "vol": Territory("Volantis", True, "The Disputed Lands"),
    "ora": Territory("The Orange Shore", True, "The Disputed Lands"),
    "tyr": Territory("Tyrosh", True, "The Disputed Lands"),
    "myr": Territory("Myr", True, "The Disputed Lands"),
    "lor": Territory("Lower Rhoyne", True, "The Disputed Lands"),
    # Andalos
    "gol": Territory("The Golden Fields", True, "Andalos"),
    "fla": Territory("The Flatlands", True, "Andalos"),
    "urh": Territory("Upper Rhoyne", True, "Andalos"),
    "axe": Territory("The Axe", True, "Andalos"),
    "foq": Territory("Forest of Qohor", True, "Andalos"),
    "bco": Territory("Braavosian Coastlands", True, "Andalos"),
    "hno": Territory("Hills of Norvos", False, "Andalos"),
    # Dothraki Sea
    "sar": Territory("Sarnor", True, "The Dothraki Sea"),
    "ndo": Territory("Northern Dothraki Sea", False, "The Dothraki Sea"),
    "wdo": Territory("Western Dothraki Sea", False, "The Dothraki Sea"),
    "edo": Territory("Eastern Dothraki Sea", False, "The Dothraki Sea"),
    "lha": Territory("Lhazar", True, "The Dothraki Sea"),
    "foo": Territory("The Footprint", False, "The Dothraki Sea"),
    "vae": Territory("Vaes Dothrak", True, "The Dothraki Sea"),
    # Jade Sea Coast
    "nar": Territory("Northern Ardor Sea", False, "Jade Sea Coast"),
    "sam": Territory("Samyrian", False, "Jade Sea Coast"),
    "say": Territory("Sayasabhad", False, "Jade Sea Coast"),
    "qar": Territory("Qarth", True, "Jade Sea Coast"),
    # Slavers' Bay
    "red": Territory("The Red Waste", False, "Slavers' Bay"),
    "old": Territory("Old Ghis", False, "Slavers' Bay"),
    "new": Territory("New Ghis", True, "Slavers' Bay"),
    "ast": Territory("Astapor", True, "Slavers' Bay"),
    "yun": Territory("Yunkai", True, "Slavers' Bay"),
    "mer": Territory("Mereen", True, "Slavers' Bay"),
    # Lands of Long Summer
    "man": Territory("Mantarys", True, "Lands of Long Summer"),
    "val": Territory("Valyria", True, "Lands of Long Summer"),
    "oro": Territory("Oros", False, "Lands of Long Summer"),
    "sea": Territory("The Sea of Sights", False, "Lands of Long Summer"),
}
regions = {
    "The Disputed Lands": Region("The Disputed Lands", 3, 6),
    "Andalos": Region("Andalos", 4, 7),
    "Slavers' Bay": Region("Slavers' Bat", 3, 6),
    "Jade Sea Coast": Region("Jade Sea Coast", 1, 4),
    "Lands of Long Summer": Region("Lands of Long Summer", 1, 4),
    "The Dothraki Sea": Region("The Dothraki Sea", 4, 7),
}

countRegion = {
    "The Disputed Lands": 0,
    "Andalos": 0,
    "Slavers' Bay": 0,
    "Jade Sea Coast": 0,
    "Lands of Long Summer": 0,
    "The Dothraki Sea": 0,
}

def checkRegion():
    global power
    for r in countRegion:
        if countRegion[r] == regions[r].terr:
            print()
            print(f"Completed region: {r}")
            if r not in complete_region:
                complete_region.append(r)
                power += regions[r].rpower
        elif countRegion[r] != regions[r].terr and r in complete_region:
                complete_region.remove(r)
                power -= regions[r].rpower
            


def reinforce_eq(power):
    forceNum = 0
    # Minmum reinforcements is 3
    if power <=11:
        forceNum += 3
    else:
        # Rule in the game to divide by three and round down
        forceNum+= power//3
    print("Reinforcements count: ", forceNum)

def printTerr():
    print("\n***TERRITORY UPDATE***\n")
    print("Your territories are: ", end = "")
    for ter in terr_data:
        print(ter.name, end= ", ")
    print()
    checkRegion()
    print()
    reinforce_eq(power)
    print()

def addTerr(string):
    global power
    myterr = [item.strip() for part in string.split(',') for item in part.split()]
    for i in myterr:
        try:
            curr_terr = territories[i]
            if curr_terr in terr_data:
                print(i + " has already been registered")
                continue
            terr_data.append(curr_terr)
            power+=1
            if curr_terr.castle == True:
                power +=1
            countRegion[curr_terr.region] += 1
        except KeyError:
            print()
            print(i + " is not a territory. Try again")
            print()
    printTerr()

def subTerr(string):
    global power
    myterr = [item.strip() for part in string.split(',') for item in part.split()]
    for i in myterr:
        try:
            curr_terr = territories[i]
            if curr_terr in terr_data:
                if curr_terr.castle == True:
                    power -=1
                terr_data.remove(curr_terr)
                power-=1
                countRegion[curr_terr.region] -= 1
                checkRegion()
        except KeyError:
            print(i + " is not a territory. Try again")
    printTerr()

def numTerr():
    print("Number of territories owned: ", len(terr_data))
    

def main():
    playing = True
    while playing:
        user_input = input("Enter command: ").lower()
        if user_input[0] == "w":
            addTerr(user_input[1:])
        if user_input[0] == "l":
            subTerr(user_input[1:])
        if user_input == 'exit' or user_input == 'q':
            playing = False
            print("Exiting game...")
        if user_input == 'num':
            numTerr()
        if user_input == 'power':
            print("Power is : ", power)
        if user_input == "help":
            with open('help.txt', 'r') as file:
                help_content = file.read()
                print(help_content)

def startTerri():
    print("To initialise your starting territories enter your currently owned territories\n"
          "Territories are taken as a 3-letter code, this is usually the first 3 letters of the name"
          " of the territory unless the name starts with 'the', then you would just input the first 3 letters"
        " of the next word")
    while len(terr_data)<CONST_ESSOS_TERR:
        initTerri = input("Input your territories seperated by a comma:\n")
        addTerr(initTerri)

                
if __name__ == "__main__":
    startTerri()
    main()