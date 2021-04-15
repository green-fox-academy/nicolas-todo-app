
FILE_NAME = "todo-list.txt"

# Usage information about the app, with the correct formatting
USAGE_INFORMATION = """
Command Line Todo application
=============================

Command line arguments:
    -l Lists all the tasks
    -a Adds a new task
    -r Removes a task
    -c Completes a task
 """


# This enumeration provides a standards for errors
class Error:
    OUT_OF_BOUND = 1
    INDEX_NOT_A_NUMBER = 2
    MISSING_INDEX = 3
    EMPTY_LIST = 4
    UNSUPPORTED_ARG = 5
    NO_TASK_PROVIDED = 6