#RiskApp

CONST_NUM_START_TERRITORY = 8
class Territory:
    def __init__(self, name: str, castle: bool, region) -> None:
        self.name = name
        self.castle = castle
        self.region = region
class Region:
    def __init__(self, name: str, power: int,) -> None:
        self.name = name
        self.power = power

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
    "The Disputed Lands": Region("The Disputed Lands", 3),
    "Andalos": Region("Andalos", 4),
    "Slaver's Bay": Region("Slavers' Bat", 3),
    "Jade Sea Coast": Region("Jade Sea Coast", 1),
    "Lands of Long Summer": Region("Lands of Long Summer", 1),
    "The Dothraki Sea": Region("The Dothraki Sea", 4),
}

def reinforce_eq(power):
    # Minmum reinforcements is 3
    if power <=11:
        return 3
    else:
        # Rule in the game to divide by three and round down
        return power//3
"""""
def main():
    playing = True
    while playing:
        user_input = input("Enter command: ").lower()

        if user_input == "":
            return 
        if user_input == 'exit' or user_input == 'q':
            playing = False
            print("Exiting game...")
        if user_input.isdigit():
            start_power = reinforce_eq(int(user_input))
            print(f'Reinforcement number: {start_power}')
        if user_input == "help":
            print("************")
            print("HELP INSTRUCTIONS")
            print("************")
            print("To manage taking of territories: After each turn record the losses and gains of"
                  " territories relevant to you in the following format\n")
            print("For gain of territories: w- xyz,... (3-letter territory code)")            
            print("For loss of territories: l- xyz,... (3-letter territory code)")
            print("Example: w- lys,vol ")
            print("Example: l- tyr,myr ")            
            print("The examples denote the gains of territories lys and volantis as well as"
                  " the losses of tyr and myr")
            print("\nTo exit the assistant type 'exit' OR press CTRL+C on your keyboard")   

"""     

def startRein():
    while True:
        starting = input("First input your starting Reinforcement "
                        "Power (number of castles): ")
        try:
            starting = int(starting)
            if starting > 0:
                print(f"Your starting reinforcement count: {reinforce_eq(starting)}")
                break 
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Is that a typo? Cmon bro")

def startTerri():
    print("To initialise your starting territories enter your currently owned territories\n"
          "Territories are taken as a 3-letter code, this is usually the first 3 letters of the name"
          " of the territory unless the name starts with 'the', then you would just input the first 3 letters"
        " of the next word")
    curr_terr = []
    power = 0
    while len(curr_terr)<3:
        initTerri = input("Input your territories seperated by a comma:\n")
        myterr = [item.strip() for part in initTerri.split(',') for item in part.split()]
        for i in myterr:
            try:
                if territories[i] in curr_terr:
                    print(i + " has already been registered")
                    continue
                curr_terr.append(territories[i])
                power+=1
                if territories[i].castle == True:
                    power +=1
            except KeyError:
                print(i + " is not a territory. Try again")
    for ter in curr_terr:
        print(ter.name, end=" ")
    print(power)

                
                
       
startTerri()
"""""
if __name__ == "__main__":
    print("*"*10)
    print("Welcome to my Risk:Game of Thrones assistant")
    print("This program is only developed for the skirmish "
          "gamemode. More will come... if/when we start playing"
          " the harder gamemode(Dominion)")
    print("You will now begin the game. Remember to keep track of your holdings. If you would "
          "like to see all commands, simply type 'help'. ") 
    print("*"*10)
    print("\n")   
    startRein()
    main()
    
    
"""