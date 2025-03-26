
file_name = "prob1-1.txt"

with open(file_name, "w") as file:
    print("Input your string...")

    while True:
        line = input(">> ")
        if line == "Q":
            break
        file.write(line + "\n")

print("Write process has been finished")