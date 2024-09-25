
To-Do List Application
Write a program to create a simple To-Do List application. The program allows
users to add tasks, view the current list of tasks, and remove tasks once they are completed.

Optional Enhancements
• Add an option in the menu that allows users to mark tasks as completed
instead of removing them. Completed tasks can be displayed separately or
removed from the list.
• Implement functionality that saves the list to a file and loads it when the
program starts. This way, users can maintain their to-do list across different sessions.
• Allow users to categorize tasks (e.g., Work, Personal) and filter the list based
on these categories. This adds an organizational element to the to-do list.


Instructions:

# Loop
# Print the menu
# Get user choice
# If choice == '1'
#   Display tasks
# Else choice == '2'
#   Add a task
#   Ask the user for a task
#   Add it to a list
# Else choice == '3'
#   Remove a task
#   Loop
#       Ask the user for a task number
#       Validate the task number
#       If invalid, print and error
#       Else remove the given task break
# Else  choice == '4'
#   Terminate/Exit/break
# Else
#   Print an error