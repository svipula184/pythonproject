# Create and write to the file
with open("student.txt", "w") as file:
    file.write("Name: S Vipula\n")
    file.write("Register Number: 24BECS184\n")
    file.write("Course: BECS\n")
    file.write("Marks: 85\n")

# Read the file
with open("student.txt", "r") as file:
    contents = file.read()

# Display the contents
print("Student Information:")
print(contents)