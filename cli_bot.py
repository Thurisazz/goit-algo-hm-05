def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Name not found, please give a correct name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please enter the name of the contact."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        return "Name not found"
    else:
        contacts[name] = phone
        return f'Contact "{name}" update: {contacts[name]}'

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
    

def show_all(contacts):
    return contacts



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Please enter a valid command")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good Bye")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    