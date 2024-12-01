left_list = []
right_list = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

differences = [abs(left - right) for left, right in zip(left_list, right_list)]
sums = sum(differences)

headers = ["Left", "Right", "Difference"]
columns = [left_list, right_list, differences]
# calulates the max width of each column to be used as padding, *unpacks the columns array
col_widths = [max(len(str(val)) for val in col) for col in [headers, *columns]]

header = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
print(header)
print("-" * len(header))

for row in zip(left_list, right_list, differences):
    formatted_row = " | ".join(
        f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row))
    )
    print(formatted_row)

print("Sum:", sums)
