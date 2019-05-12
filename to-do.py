data = []


def input_to_do(to_do_data):
    data.append(to_do_data)
    print(data)


def display_to_do():
    for i in range(len(data)):
        print(i+1, data[i])


def delete_to_do():
    display_to_do()
    number = int(input("Which to-do would you like to delete: "))
    number = number-1
    for i in range(len(data)):
        if i == number:
            data.remove(data[i])
    print(data)


def start():
    to_continue = True
    while to_continue:
        decision = input("Add, Display, Delete or Exit: ")
        if decision == "Add":
            todo = input("What would you like to add to the to-do list?: ")
            input_to_do(todo)
            to_continue = True
        elif decision == "Display":
            display_to_do()
            to_continue = True
        elif decision == "Delete":
            delete_to_do()
            to_continue = True
        elif decision == "Exit":
            to_continue = False
        else:
            print("Sorry, it wasn't clear what you wanted. Please try another input: ")
            start()


start()
print("hello")


