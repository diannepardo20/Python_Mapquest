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

        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            print("\nAPI Status: " + str(json_status) + " = A successful route call.")

            print(Fore.BLACK + Style.DIM)#FOR ADDING OF FONT COLOR AND THE OPACITY OF THE FONT
            print(Back.WHITE + "\n\n--------------------------------------------------- DIRECTIONS --------------------------------------------------")#FOR ADDING BACKGROUND HIGHLIGHT OF THE TEXT
            print(Style.RESET_ALL)#TO RESET THE STYLE ADDED AND NOT BE INHERITED BY THE NEXT LINE


            print("\nRequesting Directions from " + (orig) + " to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
            print("\n--DIRECTIONS--")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print(Fore.BLACK + Style.DIM)
            print(Back.WHITE + "\n\n----------------------------------------------- END OF DIRECTIONS -----------------------------------------------")
            print(Style.RESET_ALL)

        elif json_status == 402:
            print("-----------------------------------------------")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("-----------------------------------------------n")
        elif json_status == 611:
            print("----------------------------------------------------------------------------------------------")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("----------------------------------------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------------------------------------")
            print("For Status Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("----------------------------------------------------------------------------------------------")

    elif answer == "B" or answer == "b":#OPTION VALUE FOR OUTPUTTING INSTRUCTIONS
        print("\nInstructions: Enter the Starting and Destination point to see the directions, \nif you want to quit the application, type 'quit' or 'q' in the input fields\n")
    elif answer == "C" or answer == "C":#OPTION VALUE TO QUIT APPLICATION
        print(Fore.BLACK + Style.DIM)#FOR ADDING OF FONT COLOR AND THE OPACITY OF THE FONT
        print(Back.WHITE + "\n\n-------------------------------------------------- THANK YOU --------------------------------------------------")#FOR ADDING BACKGROUND HIGHLIGHT OF THE TEXT
        print(Style.RESET_ALL)#TO RESET THE STYLE ADDED AND NOT BE INHERITED BY THE NEXT LINE
        break
