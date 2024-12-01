from collections import Counter

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

right_counts = Counter(right_list)

appearance_counts = {num: right_counts.get(num, 0) for num in left_list}

similarity_score = [num * appearance_counts[num] for num in left_list]

total_similarity = sum(similarity_score)

headers = ["Left", "Right", "Difference", "Appearances", "Similarity"]
columns = [left_list, right_list, differences]
# calulates the max width of each column to be used as padding, *unpacks the columns array
col_widths = [
    max(len(str(val)) for val in col)
    for col in [headers, *columns, appearance_counts, similarity_score]
]

header = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
print(header)
print("-" * len(header))

for row in zip(
    left_list,
    right_list,
    differences,
    [appearance_counts[num] for num in left_list],
    similarity_score,
):
    formatted_row = " | ".join(
        f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row))
    )
    print(formatted_row)

print("Sum:", sums)

print("Total Similarity", total_similarity)
