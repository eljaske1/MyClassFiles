#-------------------------------------------------#
# Title: Homework #5
# Dev:   Erin Jaske
# Date:  March 11th, 2019
# Desc:  Create a script to import a text file, adjust the data, and 
#        then output those adjustments
#-------------------------------------------------#

#1. Create a text file called Todo.txt using the following data, one line per row:
#2. When the program starts, load each row of data from the ToDo.txt text file into a Python list. 
with open('C:\\Python\\Module05\\todo.txt') as f:
    Todo = f.read().splitlines() 
f.close()

#3. After you load the data into a list, loop through the list and add each item as a "key,value" pair a new dictionary.  
myDictTable = []
for line in Todo:
    myTasks = line.split(",")[0]
    myPriorities= line.strip('\n').split(",")[1]
    myDictionary = {myTasks: myPriorities}
    myDictTable.append(myDictionary)
print(myDictTable)

#4. After you have added existing data to the dictionary, use the menu structure 
#   included in the template to allow the user to Add or Remove tasks from the 
#   dictionary using numbered choices.
while True:
    # Display options to user
    print("""
    Menu of Options:
    1) Show current data in File
    2) Show current data in List Table
    3) Add an item to the List Table
    4) Remove an existing item from the List Table
    5) Save List Table to File
    6) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 6] - "))
    print()

# Menu, number 1: Show the current items in the File
    if (strChoice.strip() == '1'):
        print(Todo)     
        
# Menu, number 2: Show the current items in the List Table
    elif (strChoice.strip() == '2'):
        print(myDictTable)     


   
# Menu, number 3: Add a new item to the List/Table
#Create a new row for the dictionary and then add this to the dictionary 
# once user input has been received
    elif(strChoice.strip() == '3'):
        addTask = input("What household task would you like to add?: ").strip()
        addPriority = input("What is the priority level of this task? (Low/Med/High): ").strip()
        myDictRow = {addTask.strip(): addPriority.strip()}
        myDictTable.append(myDictRow)
        continue

# Menu, number 4:  Remove a new item from the list/Table
#For deleting: Use "if" statements to see if the dictionary key a user inputs 
#is in the dictionary, and if it is delete. 

    elif(strChoice == '4'):
       deleteTask = str(input("Which task do you want to remove? "))
       if deleteTask in myDictRow:
          del myDictRow[deleteTask]
          print("Task has been removed from ToDo list")
       else:
          print("Task not found")
       continue
        
    
#6. Save the data from the table into the Todo.txt file when the program exits.
# Menu, number 5: Save tasks to the ToDo.txt file
    elif(strChoice == '5'):
        objFile = open("C:\\Python\\Module05\\Todo.txt", "w")
        objFile.write(str(myDictTable))
        objFile.close()
        print("The following data was saved to a file:\n\r",myDictTable)

# Menu, number 6: Exit the Program     
    elif (strChoice == '6'):break #and Exit the program 




