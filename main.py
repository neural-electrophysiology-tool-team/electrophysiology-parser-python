# This application was developed by Michael Levi and Eyal Brand
import FileHandler

userSelection = 1

# Run main.py
# Provide a full file/folder path and follow the instructions.
while (userSelection!=0):
    try:
        isGui = False
        inputFile = FileHandler.GetFilePath()
        FileHandler.FileHandler(isGui, inputFile)
        print("\n\nTo Exit Please Press 0 or Press 1 To Continue")
        userSelection = int(input())
    except Exception as e:
        print("An exception occurred. Please Try Again")
        print(e)