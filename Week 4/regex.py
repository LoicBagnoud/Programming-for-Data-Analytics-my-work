import re

regex = "^Hello [A-Z]"
filename = "quiz.txt"

with open(filename) as quiz_file:
    for line in quiz_file:
        search_result = re.search(regex, line)
        if (search_result):
            matching_line = line
            print(matching_line, end="")