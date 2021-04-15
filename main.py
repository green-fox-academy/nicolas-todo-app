import sys
import constants
import functions


# The main function only responsible for the control flow based on the arguments
def main():
    # This is the case where no args were given
    if len(sys.argv) == 1:
        print(constants.USAGE_INFORMATION)

    # The only case where there is only one arg is the "-l" list function
    # at every other methods this case is just used for error handling
    elif len(sys.argv) == 2:

        if sys.argv[1] == "-l":
            functions.read_from_file(constants.FILE_NAME)

    # Handling the cases where the number of arguments is 3
    elif len(sys.argv) == 3:

        if sys.argv[1] == "-a":
            functions.append_to_file(constants.FILE_NAME, sys.argv[2])


if __name__ == "__main__":
    main()
