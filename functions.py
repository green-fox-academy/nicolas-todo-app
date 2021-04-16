import constants


def is_integer(variable):
    try:
        int(variable)
        return True
    except:
        return False


def row_parser(row, indicator_symbol):
    updated_row = ""
    indicator = False
    for char in row:
        if char == indicator_symbol:
            indicator = True
        if indicator:
            updated_row = updated_row + char
    return updated_row


def method_name_converter(method):
    if method == "-l":
        return "list"
    if method == "-a":
        return "add"
    if method == "-r":
        return "remove"
    if method == "-c":
        return "check"


def rebuild_list(given_list, method, chosen_row):
    counter = 1
    result_list = ""
    for row in given_list:
        if method == "remove":
            if counter < chosen_row:
                result_list = result_list + row
            elif counter > chosen_row:
                result_list = result_list + "{} {}".format(counter - 1, row_parser(row, "-"))
        elif method == "check":
            if counter == chosen_row:
                result_list = result_list + "{} - [x{}".format(counter, row_parser(row, "]"))
            else:
                result_list = result_list + row
        counter = counter + 1
    return result_list


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


def read_from_file(file_name):
    f = open("todo-list.txt", "a")
    f.close()

    current_row_number = len(open(file_name).readlines())
    f = open(file_name, "r")
    if current_row_number == 0:
        create_error("read", constants.Error.EMPTY_LIST)
    else:
        print()
        print(f.read())


def append_to_file(file_name, task):
    current_row_number = len(open(file_name).readlines())
    f = open(file_name, "a")
    f.write("{} - [ ] {}\n".format(current_row_number + 1, task))
    f.close()


def rewrite_file(file_name, chosen_row, method):
    current_rows = open(file_name).readlines()
    if len(current_rows) < chosen_row or chosen_row < 1:
        create_error(method, constants.Error.OUT_OF_BOUND)
    else:
        f = open(file_name, "w")
        f.write(rebuild_list(current_rows, method, chosen_row))
        f.close()
