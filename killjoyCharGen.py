import random
prefixes = [
    {
        "name": "Miss",
        "frequency": 1,
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Mister",
        "frequency": 1,
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Doc",
        "frequency": 1,
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Saint",
        "frequency": 1.5,
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Lady",
        "frequency": 1,
        "vibes": ["national anthem", "retro"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Lord",
        "frequency": 1,
        "vibes": ["desert punk", "rebel"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Kid",
        "frequency": 1,
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
]

# {
#         "name": "",
#         "frequency": 1,
#         "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
#         "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "neutrals", "rainbow"],
#         "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
#     },

def introText():
    vibe = 0
    role = 0
    color = 0
    while True:
        print("Welcome to the killjoy character generator!")
        print("type 'random' for a randomly generated character or 'next' to customize")
        choice = input()
        if (choice == "next"):
            while (vibe < 1 or vibe > 5):
                print("What is your Killjoy most like?")
                print("1) Neon")
                print("2) Desert Punk")
                print("3) National Anthem")
                print("4) Retro")
                print("5) Rebel")
                vibe = int(input())
                if (vibe < 1 or vibe > 5):
                    print("invalid answer, please type a number between 1 and 5")
            while (role < 1 or role > 8): 
                print("What role does your Killjoy take?")
                print("1) Scout")
                print("2) Medic")
                print("3) Nomad")
                print("4) Driver")
                print("5) Rebel")
                print("6) Messenger")
                print("7) Mechanic")
                print("8) Fighter")
                role = int(input())
                if (role < 1 or role > 8):
                    print("invalid answer, please type a number between 1 and 8")
            while (color < 1 or color > 8):
                print("What is your Killjoy's signature color?")
                print("1) Red")
                print("2) Orange")
                print("3) Yellow")
                print("4) Green")
                print("5) Blue")
                print("6) Purple")
                print("7) Pink")
                print("8) Neutrals")
                print("9) Rainbow")
                color = int(input())
                if (color < 1 or color > 9):
                    print("invalid answer, please type a number between 1 and 9")
            return vibe , role , color
        elif (choice == "random"):
            return 0 , 0 , 0
        else:
            print("invalid answer, please type 'random' or 'next'")
            
            


print(introText())