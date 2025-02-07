import sys

def list_main():    
    items = ["Java", "Python", "C#", "C", "C++", 
              ["OOP Language", "Interpreted Language", "OOP Language", "Mother of all Languages", "OOP Language"], 
              ["Python Frameworks",["Django", "Flask API"]],
              ["Java Frameworks", ["Spring Boot", "Spring Data JPA"]]]
    print_nested_list(items, True, 0)

# Print all elements of a nested list; accept if indentation is needed and the starting level of indentation
# Function arguments: items --> input list | indentation --> indetation is required or not 
#                     | level --> level of indetation starting position
def print_nested_list(items=[], indentation=False, level=0, fh=sys.stdout):
    for item in items:
        if isinstance(item, list):
            print_nested_list(item, indentation, level+1, fh)
        else:
            if indentation:
                print("\t"*level, end="", file=fh)
            print(item, file=fh)

if __name__ == "__main__":
    list_main()