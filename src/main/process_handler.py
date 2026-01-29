from src.view.first_view import introduction_page

def start() -> None:
    while True:
        command = introduction_page()
        if command == '1': print("Inserting music.")
        elif command == '2': print("Creating playlist.")
        elif command == '5': exit()
        else: print("\n Command not found, please try again. \n\n")