import re

regex = "\"([A-Z]+)\s"
filename = "access.log.txt"

with open(filename) as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len(found_text_list) != 0):
            found_text = found_text_list[0]
            print(found_text)

            print(found_text_list[1:-1])