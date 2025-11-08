"""
To-Do List Manager: Create a program to add, view, mark as complete, and delete tasks from a list/dictionary,
potentially saving the list/dictionary to a file. Please use the following as well while writing code
1.Functions
2.Modules (Optional)
3.Imports (Optional)
"""
import json
import pandas as pd


#function to create new item in list that will be called in another function
def create_new_item_in_list(data):

    day_input = input("What day of the month will you do this on?:\nDay: ")
    day = f"Day {day_input}"
    task_input = input("What will the task be?: ")
    completed = False

    new_item = {
        "Day": day,
        "Task": task_input,
        "Completed": completed
    }

    data.append(new_item)
    return(data)

    #new item has been created, just need to append it to the json file now.
    #return new_item

#print the json file to display the to do list
#along with the list itself
def print_out_to_do_list():

    df = pd.read_json('to_do_list.json')
    print(df.to_string(index=0))

#update the list to add to the list
def add_item_to_list():
    with open('to_do_list.json', 'r') as f:
        data = json.load(f)

    for _ in data:
        print(_)
    #now that it is loaded, I can append a new item to the list
    #we call the function to add a new item to the list
    create_new_item_in_list(data)

    with open('to_do_list.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Now open in read mode to read the updated data if you want to
    with open('to_do_list.json', 'r') as f:
        data = json.load(f)

    for i in data:
        print(i)



    #we've collected the new task. We need to store it in the json now.





#actions performed here
#print_out_to_do_list()
add_item_to_list()




#what I will do:
#need to hold the to do list of things in a json file
#need to read and write to the json file
#so I don't delete the other items in the list, i have to read the file, load that, append the new item
#and store it
#need to ask for options - add, view, or mark complete
#need status to show if completed or need to do
