P1 = ["Costumes", "costumes"]
P2 = ["Scenery", "scenery"]
P3 = ["Lighting", "lighting"]
P4 = ["Sound", "sound"]

def choose_practicum():
    option = input("Which practicum are you choosing? ")
    if option in P1:
        return "Costumes"
    elif option in P2:
        return "Scenery"
    elif option in P3:
        return "Lighting"
    elif option in P4:
        return "Sound"
    else:
        print("Invalid choice. Please try again.")
        return choose_practicum()

def main_function():
    name = input("What is your name?")
    practicum = choose_practicum()
    print(f"Congratulations, {name}, you are signed up for {practicum}.")

main_function()
