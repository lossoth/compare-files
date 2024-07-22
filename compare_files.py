# Read the contents of a.txt and b.txt
with open('a.txt', 'r') as file_a:
    lines_a = set(file_a.read().splitlines())

with open('b.txt', 'r') as file_b:
    lines_b = file_b.read().splitlines()

# Find lines in b.txt that are not in a.txt
unique_lines_b = [line for line in lines_b if line not in lines_a]

# Output the unique lines from b.txt
with open('unique_in_b.txt', 'w') as file_out:
    for line in unique_lines_b:
        file_out.write(line + '\n')

print("Unique lines in b.txt have been written to unique_in_b.txt")

