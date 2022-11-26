# Clearing Console

import os

os.system("cls")



# Changing Title 

import os

def title(text):
    os.system(f"title {text}")
    
    
    
# Changing Size

import os

os.system("mode 100, 50")


# Colored Print


from colorama import Fore, init

init()

print(f"{Fore.RED}This is red text, {Fore.RESET}this isnt.")



# Fade Color


from pystyle import Colors, Colorate
 
print(Colorate.Horizontal(Colors.yellow_to_red, "This is faded colored text.", 1))




# Exit Console

import os
 
os._exit(1)


# Center Text 



from pystyle import Center

print(Center.XCenter("Hello this is centered text."))
