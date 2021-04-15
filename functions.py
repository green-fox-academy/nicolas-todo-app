import constants


# Creates generic error message based on the method and on
# the type of the error. Always returns a True if it was called
# The possible errorType values are defined in the constans file
def createError(method, errorType):
    if(errorType == 1):
        print("\nUnable to {}: index is out of bound\n".format(method))
    elif(errorType == 2):
        print("\nUnable to {}: index is not a number\n".format(method))
    elif(errorType == 3):
        print("\nUnable to {}: no index provided\n".format(method))
    elif(errorType == 4):
        print("\nNo todos for today! :)\n")
    elif(errorType == 5):
        print("\nUnsupported argument")
        print(constants.USAGE_INFORMATION)
    elif(errorType == 6):
        print("\nUnable to {}: no task provided\n".format(method))
    return True



#Prints the content of the file. If the files doesn't exist, creates one
def readFromFile(fileName):
    #The following is necessary, it creates the file if it now exist yet
        f = open("todo-list.txt", "a")
        f.close()

        currentRowNumber = len(open("todo-list.txt").readlines(  ))
        f = open("todo-list.txt", "r")
        if(currentRowNumber == 0):
            createError("read", constants.Error.EMPTY_LIST)
        else:
            print()
            print(f.read())