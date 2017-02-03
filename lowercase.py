
answer = str(raw_input("Say yes or no: "))
yes = set(['yes','y'])
no = set(['no','n'])
exit = set(['exit','e'])

while True:
    if answer.lower() in yes:
        print("Thanks for saying " + answer)
        answer = raw_input("Say yes or no - say exit to quit the application: ")
    elif answer.lower() in no:
        print("Thanks for saying " + answer)
        answer = raw_input("Say yes or no - say exit to quit the application: ")
    elif answer.lower() in exit:
        print("Thanks for using this application - Goodbye!")
        break
    else:
        print("Didn't recognize your input.")
        answer = raw_input("Say yes or no - say exit to quit the application: ")
