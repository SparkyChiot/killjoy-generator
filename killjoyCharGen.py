from random import *
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
        "roles": ["any"]
    },
    {
        "name": "Captain",
        "frequency": 0.5,
        "vibes": ["desert punk", "national anthem", "retro"],
        "colors": ["any"],
        "roles": ["scout", "driver", "rebel", "fighter"]
    },
    {
        "name": "Baby",
        "frequency": 0.5,
        "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "neutrals", "rainbow"],
        "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
]

vibes = [
    "neon",
    "desert punk",
    "national anthem",
    "retro",
    "rebel",
]

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "neutrals",
    "rainbow",
]

roles = [
    "scout",
    "medic",
    "nomad",
    "driver",
    "rebel",
    "messenger",
    "mechanic",
    "fighter",
]

pronouns = [
    {
        "3rdSingular": "he",
        "objective": "him",
        "plurality": "singular"
    },
    {
        "3rdSingular": "she",
        "objective": "her",
        "plurality": "singular"
    },
    {
        "3rdSingular": "they",
        "objective": "them",
        "plurality": "plural"
    },
    {
        "3rdSingular": "it",
        "objective": "its",
        "plurality": "singular"
    },
    {
        "3rdSingular": "xey",
        "objective": "xem",
        "plurality": "plural"
    },
    {
        "3rdSingular": "fae",
        "objective": "faer",
        "plurality": "plural"
    },
    {
        "3rdSingular": "ey",
        "objective": "em",
        "plurality": "plural"
    },
]

# {
#         "name": "",
#         "frequency": 1,
#         "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
#         "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "neutrals", "rainbow"],
#         "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
#     },

def getWordsFromChoices(vibe, role, color):
    # turn vibe number into words
    if vibe == 1:
        vibe = "neon"
    elif vibe == 2:
        vibe = "desert punk"
    elif vibe == 3:
        vibe = "national anthem"
    elif vibe == 4:
        vibe = "retro"
    elif vibe == 5:
        vibe = "rebel"
    else:
        vibe = choice(vibes)
    # turn role into words
    if role == 1:
        role = "scout"
    elif role == 2:
        role = "medic"
    elif role == 3:
        role = "nomad"
    elif role == 4:
        role = "driver"
    elif role == 6:
        role = "messenger"
    elif role == 7:
        role = "mechanic"
    elif role == 8:
        role = "fighter"
    else:
        role = choice(roles)
    # turn color into words
    if color == 1:
        color = "red" 
    elif color == 2:
        color = "orange"
    elif color == 3:
        color = "yellow"
    elif color == 4:
        color = "green"
    elif color == 5:
        color = "blue"
    elif color == 6:
        color = "purple"
    elif color == 7:
        color = "pink"
    elif color == 8:
        color = "neutrals"
    elif color == 9:
        color = "rainbow"
    else:
        color = choice(colors)
    return vibe , role , color

def getNamePartFromChoices(vibe, role, color, namePart):
    namesList = []
    for each in namePart:
        matches = 0
        if vibe in each["vibes"] or "any" in each["vibes"]:
            matches += 1
    
        if role in each["roles"] or "any" in each["roles"]:
            matches += 1
        
        if color in each["colors"] or "any" in each["colors"]:
            matches += 1
        
        #append the name to the namesList * amt of matches
        for i in range(matches):
            namesList.append(each["name"])
    return choice(namesList)

def getPronounsPhrase():
    pronoun1 = choice(pronouns) 
    pronoun2 = choice(pronouns)
    if pronoun1["plurality"] == "singular":
        useTense = "uses"
    else:
        useTense = "use"
    phrase = pronoun1["3rdSingular"] + " " + useTense + " " + pronoun1["3rdSingular"] + "/" + pronoun2["objective"] + " pronouns"
    return phrase

def assembleCharacter(vibe, role, color, prefix, modifier, core, top, bottom, hobby, pronounPhrase):
    joyName = prefix + " " + modifier + " " + core
    secondColor = choice(colors)
    phrase = joyName + " is a " + vibe + " " + role + " with a " + color + " " + top + " and " + secondColor + " " + bottom + ". " + pronounPhrase + " and love " + hobby
    return phrase

def introText():
    vibe = -1
    role = -1
    color = -1
    while True:
        print("Welcome to the killjoy character generator!")
        print("type 'random' for a randomly generated character or 'next' to customize")
        choice = input()
        if (choice == "next"):
            while (vibe < 0 or vibe > 5):
                print("What is your Killjoy most like? enter zero for a random choice")
                print("1) Neon")
                print("2) Desert Punk")
                print("3) National Anthem")
                print("4) Retro")
                print("5) Rebel")
                try:
                    vibe = int(input())
                except:
                    print("invalid answer, please type a number between 0 and 5")
                if (vibe < 0 or vibe > 5):
                    print("invalid answer, please type a number between 0 and 5")
            while (role < 0 or role > 8): 
                print("What role does your Killjoy take? enter zero for a random choice")
                print("1) Scout")
                print("2) Medic")
                print("3) Nomad")
                print("4) Driver")
                print("5) Rebel")
                print("6) Messenger")
                print("7) Mechanic")
                print("8) Fighter")
                try:
                    role = int(input())
                except:
                    print("invalid answer, please type a number between 0 and 5")
                if (role < 0 or role > 8):
                    print("invalid answer, please type a number between 0 and 8")
            while (color < 0 or color > 8):
                print("What is your Killjoy's signature color? enter zero for a random choice")
                print("1) Red")
                print("2) Orange")
                print("3) Yellow")
                print("4) Green")
                print("5) Blue")
                print("6) Purple")
                print("7) Pink")
                print("8) Neutrals")
                print("9) Rainbow")
                try:
                    color = int(input())
                except:
                    print("invalid answer, please type a number between 0 and 5")
                if (color < 0 or color > 9):
                    print("invalid answer, please type a number between 0 and 9")
            return vibe , role , color
        elif (choice == "random"):
            return vibe , role , color
        else:
            print("invalid answer, please type 'random' or 'next'")
            
def main():
    vibe, role, color = introText()
    vibe, role, color = getWordsFromChoices(vibe, role, color)
    pronounPhrase = getPronounsPhrase()
    prefix = getNamePartFromChoices(vibe, role, color, prefixes)
    modifier = getNamePartFromChoices(vibe, role, color, modifiers)
    core = getNamePartFromChoices(vibe, role, color, cores)
    print(assembleCharacter(vibe, role, color, prefix, modifier, core, "shirt", "jeans", "to kill", pronounPhrase))
    

main()