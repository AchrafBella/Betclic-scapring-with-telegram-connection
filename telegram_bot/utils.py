def save_list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')

def initialize_empty_list(filename):
    # Write an empty list to the file
    save_list_to_file([], filename)

def read_list_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]
    
def update_list_and_file(new_elements, filename):
    # Read existing list from file
    existing_list = read_list_from_file(filename)
    
    # Update list with new elements
    existing_list.append(new_elements)
    
    # Save updated list to file
    save_list_to_file(existing_list, filename)
    
