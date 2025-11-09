"""
To-Do List Manager: Create a program to add, view, mark as complete, and delete tasks from a list/dictionary,
potentially saving the list/dictionary to a file. Please use the following as well while writing code
1.Functions
2.Modules (Optional)
3.Imports (Optional)
"""

import json
import pandas as pd
import os

# function to read out the to do list every time it is called
# print the json file to display the to do list
# along with the list itself
def print_out_to_do_list():

    print("To do list: ")
    df = pd.read_json('to_do_list.json')
    print(df.to_string(index=0))



# this function will simply display options. it does not return anything.
def display_options():

    print("*****************(To-do list)*****************")
    print("Please select a number: ")
    print("1. Add to the list: ")
    print("2. View the list: ")
    print("3. Mark an item on your list as complete: ")
    print("4. Delete an item from your list: ")
    print("**********************************************")



#function to create new item in list that will be called in another function
def create_new_item_in_list(data):

    day_input = input("What day of the month will you do this on?:\nDay: ")
    day = f"Day {day_input}"
    task_input = input("What will the task be?: ")
    completed = "No"

    new_item = {
        "Day": day,
        "Task": task_input,
        "Completed": completed
    }

    #append the new_item to the data and return that data.
    #the data will be added to the json file in the other function
    data.append(new_item)
    return(data)



#need a function that marks the item as complete
def mark_item_complete():

    # need to access the specific day
    with open("to_do_list.json", 'r') as f:
        data = json.load(f)

    # display the list
    print_out_to_do_list()

    # change the value from "no" to "yes"
    day_input = input("Select which day you want to mark as complete: ")
    day_key = f"Day {day_input}"

    for item in data:
        if item["Day"] == day_key:
            item["Completed"] = "Yes"
            break

    # save the updated list

    with open("to_do_list.json", 'w') as f:
        json.dump(data, f, indent=4)


# for this one, I need to display all days
# allow user to select which day he would like to mark as complete
def delete_item_from_list():

    # load the list for user to see which one they need to delete
    print_out_to_do_list()

    print("Please select which task you wish to delete with the corresponding day number:\nDay ")
    day_num = input("Day ")
    day_to_delete = (f"Day {day_num}")

    #we need to load the data here and filter out the correct day and save the list as a whole
    with open('to_do_list.json', 'r') as f:
        data = json.load(f)

    #filter the data and update json file
    data = [item for item in data if item["Day"] != day_to_delete]
    with open('to_do_list.json', 'w') as f:
        json.dump(data, f, indent=4)

    #if they do not have anything to mark complete, they can select "back"


#update the list to add to the list
def add_item_to_list():

    print("Add to your to-do list: ")

    with open('to_do_list.json', 'r') as f:
        data = json.load(f)

    #now that it is loaded, I can append a new item to the list
    #we call the function to add a new item to the list
    create_new_item_in_list(data)

    # writing the appended list to json file
    with open('to_do_list.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Now open in read mode to read the updated data
    with open('to_do_list.json', 'r') as f:
        data = json.load(f)



    #this is where we will call everything
print("Hello, welcome to your to-do list!")

#selection
end = "n"

while(end == "n"):

    os.system('cls' if os.name == 'nt' else 'clear')

    display_options()
    selection = int(input("Enter your selection: "))

    if (selection == 1):
        add_item_to_list()
    elif(selection == 2):
        print_out_to_do_list()
    elif(selection == 3):
        mark_item_complete()
        pass
    elif(selection == 4):
        delete_item_from_list()

    end = input("Exit out of todo list?: (y/n): ")#actions performed here
