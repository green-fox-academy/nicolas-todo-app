import constants


# Creates generic error message based on the method and on
# the type of the error. Always returns a True if it was called
# The possible errorType values are defined in the constans file
def create_error(method, error_type):
    if error_type == 1:
        print("\nUnable to {}: index is out of bound\n".format(method))
    elif error_type == 2:
        print("\nUnable to {}: index is not a number\n".format(method))
    elif error_type == 3:
        print("\nUnable to {}: no index provided\n".format(method))
    elif error_type == 4:
        print("\nNo todos for today! :)\n")
    elif error_type == 5:
        print("\nUnsupported argument")
        print(constants.USAGE_INFORMATION)
    elif error_type == 6:
        print("\nUnable to {}: no task provided\n".format(method))
    return True


# Prints the content of the file. If the files doesn't exist, creates one
def read_from_file(file_name):
    # The following is necessary, it creates the file if it now exist yet
    f = open("todo-list.txt", "a")
    f.close()

    current_row_number = len(open(file_name).readlines())
    f = open(file_name, "r")
    if current_row_number == 0:
        create_error("read", constants.Error.EMPTY_LIST)
    else:
        print()
        print(f.read())


# Writes at the end of the file
def append_to_file(file_name, task):
    current_row_number = len(open(file_name).readlines())
    f = open(file_name, "a")
    f.write("{} - [ ] {}\n".format(current_row_number + 1, task))
    f.close()
