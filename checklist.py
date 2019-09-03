# CREATE CHECKLIST
checklist = list()


# DEFINE FUNCTIONS:
# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# MARK COMPLETED
def mark_completed(index):
    return (index, "√" + checklist[item])

# SELECTION
def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    # READ ITEM
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(int(item_index))
        return True
   
    # UPDATE ITEM
    elif function_code == "U":
            item_index = user_input("Index Number?")
            input_item = user_input("Edit item:")
            return True

    # PRINT ALL ITEMS
    elif function_code == "P":
        list_all_items()
        return True
    
    # QUIT GAME
    elif function_code == "Q":
        return False

    # CATCH ALL
    else:
        print("Unknown Option")
    return True

# USER_INPUT
def user_input(prompt):
    # the input function will display a message in the terminal and wait for user input.
    user_input = input(prompt)
    return user_input


# TEST
def test():
    create("purple sox")
    create("red cloak")

#     print(read(0))
#     print(read(1))

#     update(0, "purple socks")
#     destroy(1)

#     print(read(0))
#     select("C")

#     list_all_items()

#     select("R")

#     list_all_items()


# user_value = user_input("Please Enter a value:")
# print(user_value)


test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, U to update list item, D to delete list item, P to display list, and Q to quit: ")
    running = select(selection)
