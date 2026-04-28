from random import *
prefixes = [
    {
        "name": "Miss",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Mister",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Doc",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Saint",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Lady",
        "vibes": ["any", "national anthem", "retro"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Lord",
        "vibes": ["any" "desert punk", "rebel"],
        "colors": ["any", "purple"],
        "roles": ["any"]
    },
    {
        "name": "Kid",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "Captain",
        "vibes": ["desert punk", "national anthem", "retro"],
        "colors": ["any"],
        "roles": ["any", "scout", "driver", "rebel", "fighter"]
    },
    {
        "name": "Baby",
        "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "Neutral", "rainbow"],
        "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "Queen",
        "vibes": ["any", "national anthem", "retro"],
        "colors": ["any", "purple"],
        "roles": ["any", "nomad", "driver", "fighter"]
    },
    {
        "name": "Agent",
        "vibes": ["any", "neon", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "rebel", "messenger", "fighter"]
    },
    {
        "name": "Sister",
        "vibes": ["any", "retro"],
        "colors": ["any", "pink", "Neutral"],
        "roles": ["any", "medic", "nomad", "driver"]
    },
    {
        "name": "Reverend",
        "vibes": ["desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any"],
        "roles": ["any", "scout", "medic", "nomad", "rebel", "messenger"]
    },
    {
        "name": "Mother",
        "vibes": ["any", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "purple", "pink"],
        "roles": ["any"]
    },
    {
        "name": "Sheriff",
        "vibes": ["any", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
]

modifiers = [
    {
        "name": "Static",
        "vibes": ["neon", "retro"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "nomad", "rebel", "fighter"]
    },
    {
        "name": "Rust",
        "vibes": ["desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange",],
        "roles": ["any", "mechanic",]
    },
    {
        "name": "Neon",
        "vibes": ["neon", "national anthem"],
        "colors": ["red", "orange", "yellow", "green", "blue", "purple", "pink", "rainbow"],
        "roles": ["any"]
    },
    {
        "name": "Acid",
        "vibes": ["any", "neon"],
        "colors": ["any", "green"],
        "roles": ["any"]
    },
    {
        "name": "Ash",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["red", "Neutral"],
        "roles": ["any", "fighter"]
    },
    {
        "name": "Ghost",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "nomad", "fighter"]
    },
    {
        "name": "Velvet",
        "vibes": ["national anthem", "retro"],
        "colors": ["any", "red", "purple"],
        "roles": ["any"]
    },
    {
        "name": "Chrome",
        "vibes": ["neon", "retro", "rebel"],
        "colors": ["any", "Neutral", "rainbow"],
        "roles": ["any", "driver"]
    },
    {
        "name": "Hollow",
        "vibes": ["desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "nomad", "rebel"]
    },
    {
        "name": "Riot",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any", "red"],
        "roles": ["any", "rebel", "fighter"]
    },
]

cores = [
    {
        "name": "Motel",
        "vibes": ["neon", "national anthem", "retro"],
        "colors": ["any"],
        "roles": ["any", "driver", "rebel"]
    },
    {
        "name": "Knife",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["any", "fighter"]
    },
    {
        "name": "Radio",
        "vibes": ["any", "neon", "retro", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "driver", "messenger"]
    },
    {
        "name": "Petal",
        "vibes": ["any", "desert punk", "national anthem"],
        "colors": ["any", "pink", "rainbow"],
        "roles": ["any", "nomad", "driver"]
    },
]

clothingModifiers = [
    {
        "name": "Distressed",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "nomad", "rebel", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "Weathered",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "rebel", "fighter"]
    },
    {
        "name": "Pristine",
        "vibes": ["any", "neon", "retro"],
        "colors": ["any"],
        "roles": ["any", "medic", "driver", "messenger"]
    },
    {
        "name": "Embroidered",
        "vibes": ["any"],
        "colors": ["any", "rainbow"],
        "roles": ["any"]
    },
    {
        "name": "Frayed",
        "vibes": ["any", "desert punk", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "nomad", "rebel", "mechanic", "fighter"]
    },
    {
        "name": "Ripped",
        "vibes": ["any", "neon", "desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["any", "scout", "nomad", "rebel", "mechanic", "fighter"]
    },
    {
        "name": "Patchwork",
        "vibes": ["any","desert punk", "national anthem"],
        "colors": ["any", "red", "Neutral", "rainbow"],
        "roles": ["any", "scout", "medic", "nomad", "rebel", "mechanic"]
    },
    {
        "name": "Oversized",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any", "nomad", "rebel", "messenger"]
    },
    {
        "name": "Fitted",
        "vibes": ["any", "neon", "national anthem", "retro", "rebel"],
        "colors": ["any"],
        "roles": ["any", "medic", "driver", "mechanic", "fighter"]
    },
]

clothingMaterials = [
    {
        "name": "Cotton",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any"],
        "roles": ["any", "scout", "medic", "messenger", "mechanic"]
    },
    {
        "name": "Linen",
        "vibes": ["any", "desert punk", "retro", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "nomad", "messenger"]
    },
    {
        "name": "Silk",
        "vibes": ["neon", "national anthem", "retro"],
        "colors": ["any", "pink", "Neutral"],
        "roles": ["any", "medic", "nomad", "driver", "messenger"]
    },
    {
        "name": "Canvas",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "rebel", "messenger", "mechanic"]
    },
    {
        "name": "Suede",
        "vibes": ["any", "desert punk", "retro", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "driver", "messenger", "mechanic"]
    },
    {
        "name": "Leather",
        "vibes": ["any"],
        "colors": ["any", "red", "Neutral"],
        "roles": ["any", "driver", "rebel", "mechanic", "fighter"]
    },
]

tops = [
    {
        "name": "crewneck tee",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any", "scout", "driver", "fighter"]
    },
    {
        "name": "v-neck shirt",
        "vibes": ["any", "neon", "retro"],
        "colors": ["any"],
        "roles": ["any", "driver", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "muscle shirt",
        "vibes": ["desert punk", "national anthem", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["scout", "rebel", "mechanic", "fighter"]
    },
    {
        "name": "racerback tank",
        "vibes": ["neon", "desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["driver", "rebel", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "spaghetti strap tank",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["scout", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "polo shirt",
        "vibes": ["any", "retro"],
        "colors": ["any", "green", "blue", "purple", "pink", "Neutral"],
        "roles": ["scout", "medic", "driver", "messenger"]
    },
    {
        "name": "hoodie",
        "vibes": ["any", "neon", "desert punk", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["scout", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },
    {
        "name": "crewneck sweatshirt",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any"],
        "roles": ["any"]
    },
]

bottoms = [
    {
        "name": "jeans",
        "vibes": ["any"],
        "colors": ["any", "blue", "Neutral"],
        "roles": ["any", "medic", "driver", "rebel", "messenger", "mechanic"]
    },
    {
        "name": "cargo pants",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any"]
    },
    {
        "name": "leggings",
        "vibes": ["any", "neon"],
        "colors": ["any", "Neutral", "rainbow"],
        "roles": ["any"]
    },
    {
        "name": "sweatpants",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "nomad", "messenger"]
    },
    {
        "name": "shorts",
        "vibes": ["any"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "nomad", "driver", "rebel", "messenger"]
    },
    {
        "name": "cargo shorts",
        "vibes": ["any", "desert punk", "rebel"],
        "colors": ["any", "Neutral"],
        "roles": ["any"]
    },
    {
        "name": "trousers",
        "vibes": ["desert punk", "national anthem", "retro"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "medic", "driver", "messenger"]
    },
]

accessories = [
    {
        "name": "blazer",
        "vibes": ["any", "desert punk", "national anthem", "retro"],
        "colors": ["any", "blue", "Neutral"],
        "roles": ["any", "medic", "driver", "messenger"]
    },
    {
        "name": "cardigan",
        "vibes": ["any", "desert punk", "retro"],
        "colors": ["any", "Neutral", "rainbow"],
        "roles": ["any", "medic", "nomad", "messenger"]
    },
    {
        "name": "vest",
        "vibes": ["any"],
        "colors": ["any"],
        "roles": ["any"]
    },
    {
        "name": "waistcoat",
        "vibes": ["any", "desert punk", "retro"],
        "colors": ["any", "red", "green", "blue", "purple", "Neutral"],
        "roles": ["any", "scout", "medic", "nomad", "fighter"]
    },
]

hobbies = [
    {
        "name": "scour the zones for vintage tech",
        "vibes": ["any"],
        "colors": ["any", "Neutral"],
        "roles": ["any", "scout", "nomad", "mechanic"]
    },
    {
        "name": "hotwire abandoned cars",
        "vibes": ["any", "desert punk", "national anthem", "rebel"],
        "colors": ["any"],
        "roles": ["any", "nomad", "driver", "rebel", "mechanic"]
    },
    {
        "name": "make armor out of scrap metal",
        "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "Neutral", "rainbow"],
        "roles": ["any", "nomad", "driver", "rebel", "fighter"]
    },
    {
        "name": "tag ruins with spray paint",
        "vibes": ["any", "neon", "desert punk"],
        "colors": ["any", "rainbow"],
        "roles": ["any", "scout", "nomad", "rebel", "fighter"]
    },
    {
        "name": "broadcast pirate radio signals",
        "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "Neutral", "rainbow"],
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
    "Neutral",
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
        "plurality": "singular",
    },
    {
        "3rdSingular": "she",
        "objective": "her",
        "plurality": "singular",
    },
    {
        "3rdSingular": "they",
        "objective": "them",
        "plurality": "plural",
    },
    {
        "3rdSingular": "it",
        "objective": "its",
        "plurality": "singular",
    },
    {
        "3rdSingular": "xey",
        "objective": "xem",
        "plurality": "plural",
    },
    {
        "3rdSingular": "fae",
        "objective": "faer",
        "plurality": "plural",
    },
    {
        "3rdSingular": "ey",
        "objective": "em",
        "plurality": "plural",
    },
]

{
        "name": "",
        "vibes": ["any", "neon", "desert punk", "national anthem", "retro", "rebel"],
        "colors": ["any", "red", "orange", "yellow", "green", "blue", "purple", "pink", "Neutral", "rainbow"],
        "roles": ["any", "scout", "medic", "nomad", "driver", "rebel", "messenger", "mechanic", "fighter"]
    },

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
        color = "Neutral"
    elif color == 9:
        color = "rainbow"
    else:
        color = choice(colors)
    return vibe , role , color

def getPartFromChoices(vibe, role, color, part):
    namesList = []
    for each in part:
        matches = 0
        if vibe in each["vibes"] and "any" in each["vibes"]:
            matches += 2
        elif vibe in each["vibes"] or "any" in each["vibes"]:
            matches += 1

        if role in each["roles"] and "any" in each["roles"]:
            matches += 2
        elif role in each["roles"] or "any" in each["roles"]:
            matches += 1
        
        if color in each["colors"] and "any" in each["colors"]:
            matches += 2
        elif color in each["colors"] or "any" in each["colors"]:
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
        loveForm = "loves"
    else:
        useTense = "use"
        loveForm = "love"
    phrase = pronoun1["3rdSingular"] + " " + useTense + " " + pronoun1["3rdSingular"] + "/" + pronoun2["objective"] + " pronouns and " + loveForm + " to "
    return phrase



def assembleCharacter(vibe, role, color, prefix, modifier, core, top, bottom, hobby, pronounPhrase):
    joyName = prefix + " " + modifier + " " + core
    secondColor = choice(colors)
    phrase = joyName + " is a " + vibe + " " + role + " with a " + color + " " + top + " and " + secondColor + " " + bottom + ". " + pronounPhrase + hobby
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
                print("8) Neutral")
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
    prefix = getPartFromChoices(vibe, role, color, prefixes)
    modifier = getPartFromChoices(vibe, role, color, modifiers)
    core = getPartFromChoices(vibe, role, color, cores)
    top = getPartFromChoices(vibe, role, color, clothingModifiers) + " " + getPartFromChoices(vibe, role, color, clothingMaterials) + " " + getPartFromChoices(vibe, role, color, tops)
    bottom = getPartFromChoices(vibe, role, color, clothingModifiers) + " " + getPartFromChoices(vibe, role, color, clothingMaterials) + " " + getPartFromChoices(vibe, role, color, bottoms)
    hobby = getPartFromChoices(vibe, role, color, hobbies)
    # decide how many name parts to use
    diceRoll = randint(1,100)
    if diceRoll >= 45:
        prefix = ""
    diceRoll = randint(1,100)
    if diceRoll >= 80:
        modifier = ""
    diceRoll = randint(1,100)
    if diceRoll <= 10:
        modifier = "" 
        prefix = ""
    # if vibe and role = rebel, reroll
    while vibe == role:
        if vibe == role:
            role = choice(roles)
    print(assembleCharacter(vibe, role, color, prefix, modifier, core, top, bottom, hobby, pronounPhrase))
    

main()
