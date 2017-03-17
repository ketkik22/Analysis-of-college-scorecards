# Configuration file to hold certain settings which can vary depending on one's own MongoDB server set-up

MONGODB_HOST_NAME = '171.168.33.10'
MONGODB_PORT_NUMBER = 27077
MONGODB_COLLEGE_SCORE_DATABASE_NAME = 'collegeTemp'
MONGODB_COLLEGE_SCORE_COLLECTION_NAME = 'collegeData'

MONGODB_CONNECTION_ATTEMPT_LENGTH_MS = 5000  # How many milliseconds to try establish connection with MongoDB database

NUM_LINES_TO_PRINT = 10  # How many lines at a time to print results to console

EXIT_SHELL_VALUE = -1  # Value user enters into program to indicate they want to exit
NUMBER_OF_QUERIES = 16  # Total number of queries currently listed as options in the program
SHOW_OPTIONS_VALUE = 0  # Value user enters into program to indicate they want to see all options again
