import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "1fRfZdxZ6MksxGxYZ8k81IeaR9ASo5pI"

from colorama import Fore, Back, Style
print(Fore.BLACK + Style.DIM) #FOR ADDING OF FONT COLOR AND THE OPACITY OF THE FONT
print(Back.WHITE + "\n\n---------------------------------------- MAPQUEST DIRECTIONS APPLICATION ---------------------------------------")#FOR ADDING BACKGROUND HIGHLIGHT OF THE TEXT
print(Style.RESET_ALL)#TO RESET THE STYLE ADDED AND NOT BE INHERITED BY THE NEXT LINE

while True:
    answer = input("\nChoose on what you want to do \n\nA.Start MAPQUEST Application\nB.How to use the application \nC.Quit\n\nAnswer: ") #TO OUTPUT OPTION VALUES

    if answer == "A" or answer == "a": #OPTION VALUE
        orig = input("\n\nStarting Location: ")
        if orig == "quit" or orig == "q":
            break
        dest = input("\nDestination: ")
        if dest == "quit" or dest == "q":
            break
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) #TO GENERATE MAPQUEST LINK
        json_data = requests.get(url).json()
        print("\nURL: " + (url)) #TO OUTPUT MAPQUEST LINK
        json_data = requests.get(url).json()
