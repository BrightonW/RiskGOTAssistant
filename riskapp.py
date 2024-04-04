#RiskApp
class Territory:
    def __init__(self, name: str, castle: bool, region) -> None:
        self.name = name
        self.castle = castle
        self.region = region
class Region:
    def __init__(self, name: str, sub_terr: list) -> None:
        self.name = name
        self.sub_terr = sub_terr

# Define territories and regions using dictionaries
territories = {
    "lys": Territory("Lys", False, "The Disputed Lands"),
    "vol": Territory("Volantis", True, "The Disputed Lands"),
    "ora": Territory("The Orange Shore", True, "The Disputed Lands"),
    "tyr": Territory("Tyrosh", True, "The Disputed Lands"),
    "myr": Territory("Myr", True, "The Disputed Lands"),
    "lor": Territory("Lower Rhoyne", True, "The Disputed Lands"),

    "gol": Territory("The Golden Fields", True, "Andalos"),
    "fla": Territory("The Flatlands", True, "Andalos"),
    "urh": Territory("Upper Rhoyne", True, "Andalos"),
    "axe": Territory("The Axe", True, "Andalos"),
    "foq": Territory("Forest of Qohor", True, "Andalos"),
    "bco": Territory("Braavosian Coastlands", True, "Andalos"),
    "hno": Territory("Hills of Norvos", False, "Andalos"),

    "sar": Territory("Sarnor", True, "Andalos"),
    # Add more territories as needed
}

regions = {
    "The Disputed Lands": Region("The Disputed Lands", []),
    # Add more regions as needed
}

def reinforce_eq(power):
    if power <=11:
        return 3
    else:
        # Rule in the game to divide by three and round down
        return power//3

def main():
    playing = True
    while playing:
        user_input = input("Enter command: ").lower()

        if user_input == "i":
            return 
        if user_input == 'exit' or user_input == 'q':
            playing = False
            print("Exiting game...")
            break

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

def startRein():
    starting = int(input("First input your starting Reinforcement "
            "Power(number of castles): "))
    if  starting>0:
        print(f"You're starting reinforcement count: {reinforce_eq(starting)}")
    else:
        print("Invalid Entry")
        starting = int(input("First input your starting Reinforcement "
            "Power(number of castles): ")) 

def startTerri():
    print("To initialise your starting territories enter your currently owned territories\n"
          "Territories are taken as a 3-letter code, this is usually the first 3 letters of the name"
          " of the territory unless the name starts with 'the', then you would just input the first 3 letters"
        " of the next word")
    initTerri = input("Input your territories seperated by a comma:\n")
    myterr = [item.strip() for part in initTerri.split(',') for item in part.split()]
    return   

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
    
    
    