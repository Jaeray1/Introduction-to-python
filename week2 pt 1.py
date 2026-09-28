# List - Mutable, allows duplicates
my_list = ["Python", "GenAI", "Python"]
my_list.append("IDLE")
print("List:", my_list)

# Tuple - Immutable, allows duplicates
my_tuple = ("Python", "GenAI")
print("Tuple:", my_tuple)

# Set - Unique values only
my_set = {"Python", "GenAI", "Python"}
my_set.add("IDLE")
print("Set:", my_set)

# DMS - if, elif, else
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

# FCS - break, continue, pass
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break  # stop loop
    print(i)

# For loop + Nested If + Flow Control
numbers = [95, 82, 35, 88, 40]

for marks in numbers:
    if marks >= 80:  # DMS
        print(f"{marks} - Pass")
        if marks > 90:  # Nested If
            print("-> Topper!")
    else:
        if marks < 40:  # DMS
            print(f"{marks} - Fail")
            continue  # FCS - skip

print("Loop Completed")
