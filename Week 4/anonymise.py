import re

regex = r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" 

replacement_text = "\\1XXX.XXX"
filename = "access.log.txt"
output_file_name = "anonymisedIPs.txt"

with open(filename) as input_file:
    with open(output_file_name, "w") as output_file:
        for line in input_file:
            new_line = re.sub(regex, replacement_text, line)
            output_file.write(new_line)

print(f"The new anonymised file name {output_file_name} has been created in the folder.")