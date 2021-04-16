import sys
import constants
import functions


def main():
    if len(sys.argv) == 1:
        print(constants.USAGE_INFORMATION)

    elif len(sys.argv) == 2:

        if sys.argv[1] == "-l":
            functions.read_from_file(constants.FILE_NAME)

        elif sys.argv[1] == "-a":
            functions.create_error(functions.method_name_converter(sys.argv[1]), constants.Error.NO_TASK_PROVIDED)

        else:
            functions.create_error(None, constants.Error.UNSUPPORTED_ARG)

    elif len(sys.argv) == 3:

        if sys.argv[1] == "-a":
            functions.append_to_file(constants.FILE_NAME, sys.argv[2])

        elif (sys.argv[1] == "-r") or (sys.argv[1] == "-c"):
            if functions.is_integer(sys.argv[2]):
                functions.rewrite_file(constants.FILE_NAME, int(sys.argv[2]), functions.method_name_converter(sys.argv[1]))
            else:
                functions.create_error(functions.method_name_converter(sys.argv[1]), constants.Error.INDEX_NOT_A_NUMBER)
        else:
            functions.create_error(None, constants.Error.UNSUPPORTED_ARG)

    else:
        functions.create_error(None, constants.Error.UNSUPPORTED_ARG)


if __name__ == "__main__":
    main()
