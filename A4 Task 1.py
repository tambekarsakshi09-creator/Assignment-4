try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print the file line by line
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # Handle the error if file does not exist
    print("Error: The file 'sample.txt' does not exist.")
