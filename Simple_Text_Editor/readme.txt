Simple Text Editor
Write a program to create a simple text editor. This program allows users to open
an existing text file or create a new one, edit the content, and then save the
changes by typing the SAVE command.

Optional Enhancements
• Allow users to choose whether they want to overwrite the existing file content
or append new text to the end of the file.
• Add functionality to search for specific words or phrases in the text and replace them with new content.

Instructions:

# Ask the user for a filename
# If file exists
#   Open it
#   Write its content to the terminal
# Else
#   Create a new file
# If file cant be open
#   Print and error
# Loop
#   Get user input
#   If input == "SAVE":
#       Break
# Write all the user input into the file