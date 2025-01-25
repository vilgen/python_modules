def list_main():    
    items = ["Java", "Python", "C#", "C", "C++", 
              ["OOP Language", "Interpreted Language", "OOP Language", "Mother of all Languages", "OOP Language"], 
              ["Python Frameworks",["Django", "Flask API"]],
              ["Java Frameworks", ["Spring Boot", "Spring Data JPA"]]]
    print_nested_list(items, True, 0)

# Print all elements of a nested list; accept if indentation is needed and the starting level of indentation
# Function arguments: items --> input list | indentation --> indetation is required or not 
#                     | level --> level of indetation starting position
def print_nested_list(items=[], indentation=False, level=0):
    for item in items:
        if isinstance(item, list):
            print_nested_list(item, indentation, level+1)
        else:
            if indentation:
                print("\t"*level, end="")
            print(item)

list_main()