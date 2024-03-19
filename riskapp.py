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
    "tos": Territory("The Orange Shore", True, "The Disputed Lands"),
    "tyr": Territory("Tyrosh", True, "The Disputed Lands"),
    "myr": Territory("Myr", True, "The Disputed Lands"),
    "lrh": Territory("Lower Rhoyne", True, "The Disputed Lands"),

    "gof": Territory("The Golden Fields", True, "Andalos"),
    "fla": Territory("The Flatlands", True, "Andalos"),
    "urh": Territory("Upper Rhoyne", True, "Andalos"),
    "axe": Territory("The Axe", True, "Andalos"),
    "foq": Territory("Forest of Qohor", True, "Andalos"),
    "bco": Territory("Braavosian Coastlands", True, "Andalos"),
    "hno": Territory("Hills of Norvos", False, "Andalos"),

    "urh": Territory("Sarnor", True, "Andalos"),

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
        return power//3

def main():
    playing = True
    while playing:
        user_input = input("Enter command: ").lower()

        if user_input == "":
            return 
        if user_input == 'exit':
            playing = False
            print("Exiting game...")
            break
        if user_input.isdigit():
            start_power = reinforce_eq(int(user_input))
            print(f'Reinforcement number: {start_power}')
        if user_input == "help":
            
            return
if __name__ == "__main__":
    print("*"*8)
    print("Welcome to my Risk:Game of Thrones assistant")
    print("This program is only developed for the skirmish "
          "gamemode. More will come... if/when we start playing"
          " the harder gamemode(Dominion)")
    print("*"*8)
    starting = int(input("First input your starting Reinforcement "
            "Power(number of castles): "))
    start_rein = reinforce_eq(starting)
    print("Starting reinforcement count: " ,start_rein)
    print("You will now begin the game. Remember to keep track of your holdings. If you would "
          "like to see all commands, simply type 'help'. ")    
    main()
    
    
    