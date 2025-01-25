def file_main():
    read_file_content_to_list("sketch.txt")

# Gets a file name, opens it, reads the data to tuples (immutable list) by splitting it with : char, 
# print the modified result to the console
def read_file_content_to_list(file):
    try:
        data = open(file)
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", maxsplit=1)
                print(role, end="")
                print(" said: ", end="")
                print(line_spoken, end="")
            except ValueError:
                pass
        data.close()
    except IOError:
        print("File can't be read!")


file_main()