from termcolor import colored, cprint

def draw_house():
    house = [
        "   /\ ---------------\ ",
        "  /  \                \ ",
        " /    \                \ ",
        "/------\ ---------------\ ",
        "|      |               |",
        "|      |               |",
        "------------------------"
    ]

    for line in house:
        cprint(line, 'blue')

draw_house()