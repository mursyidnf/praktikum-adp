from termcolor import colored, cprint

width = 35  
height = 5 

for _ in range(height):
    cprint(' ' * width, 'white', 'on_red')

for _ in range(height):
    cprint(' ' * width, 'grey', 'on_white')