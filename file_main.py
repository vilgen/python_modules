from list_main import print_nested_list
import pickle

def file_main():
    read_data_from_file_write_to_two_files("sketch.txt")
    read_data_from_binary_files()

# Gets a file name, opens it, reads the data to tuples (immutable list) by splitting it with : char, 
# print the modified result to 2 different files console
def read_data_from_file_write_to_two_files(file):
    man = []
    other = []
    try:
        with open(file) as data:
            for each_line in data:
                try:
                    (role, line_spoken) = each_line.split(":", maxsplit=1)
                    line_spoken = line_spoken.strip()
                    if role == "Man":
                        man.append(line_spoken)
                    elif role == "Other Man":
                        other.append(line_spoken)
                except ValueError:
                    pass
        # Write data to text files
        with open("man_data.txt", "w") as man_file, open("other_file.txt", "w") as other_file:
             print_nested_list(man, fh=man_file)
             print_nested_list(other, fh=other_file)
        # Write data to binary files
        with open("man_data_binary.txt", "wb") as man_file_binary, open("other_file_binary.txt", "wb") as other_file_binary:
             pickle.dump(man, man_file_binary)
             pickle.dump(other, other_file_binary)
    
    except IOError as err:
        print("File err: " + str(err))
    except pickle.PickleError as err:
        print("Pickle err: " + str(err))

# Read data from binary files
def read_data_from_binary_files():
    try:
        with open("man_data_binary.txt", "rb") as man_file_binary, open("other_file_binary.txt", "rb") as other_file_binary:
            man = pickle.load(man_file_binary)
            other = pickle.load(other_file_binary)  
            print_nested_list(man)
            print_nested_list(other)
    except IOError as err:
        print("File err: " + str(err))
    except pickle.PickleError as err:
        print("Pickle err: " + str(err))       

                
if __name__ == "__main__":
    file_main()