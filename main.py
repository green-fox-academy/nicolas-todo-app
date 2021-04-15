import sys
import constants


# The main function only responsible for the control flow based on the arguments
def main():
    # This is the case where no args were given
    if (len(sys.argv) == 1):
        print(constants.USAGE_INFORMATION)

if __name__ == "__main__":
    main()
