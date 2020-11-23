data = []

def addNote():
    title = input("Title note. ")
    content = input("Input contents. ")
    data.append([title, content])
    print("Note added.")

def deleteNote():
    index = int(input("Input index."))
    data.pop(index - 1)

def listNotes():
    for i in data:
        print("Title: " + i[0])
        print("Contents: " + i[1])
        print("")

def printNote():
    i = int(input("Input index.")) - 1
    print("Title: " + data[i][0])
    print("Contents: " + data[i][1])
    

def main():

    command = input(("Input a to add a note. Input d to delete a note. Input l to list notes. Input p to print a note. Input q to quit. "))
    print("")

    while(command != "q"):

        if(command == "a"):
            addNote()
        
        elif(command == "d"):
            deleteNote()
        
        elif(command == "l"):
            listNotes()

        elif(command == "p"):
            printNote()

        else:
            print("Error. Input again.")
        
        command = input(("Input a to add a note. Input d to delete a note. Input l to list notes. Input p to print a note. Input q to quit. "))
        print("")
    
    exit

main()