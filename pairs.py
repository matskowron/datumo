import re
from typing import Sequence

def find_pairs(input: Sequence[int]) -> Sequence[int]:

    SUM_TO = 12

    assert input, "Provided not correct list. The list should contain only integers"
    for element in input:
        assert element >= 0, f"Element {element} is smaller than 0"
        assert element <= 12, f"Element {element} is greater than 12"


    output = []

    # Creating an array for each integer in the list 
    # numerical complexity = O(n);
    count_array = [0] * (SUM_TO + 1)

    # Adding the +1 to ha
    # numerical complexity = O(n);
    for number in input: 
        count_array[number] = count_array[number] + 1 

    # Iterating till the "median" of the array
    for i in range(0, SUM_TO // 2 + 1): 
        
        missing_to_i = SUM_TO - i
        
        if (count_array[i] > 1 and count_array[missing_to_i] > 1 and i != missing_to_i):
            output += ((i, missing_to_i),(i, missing_to_i))

        elif (count_array[i] > 0 and count_array[missing_to_i] > 0):
            output.append((i, missing_to_i))
        
    return output


def open_file(file_name="input.txt"):
    
    assert TypeError, "No file name provided."

    print(f"The script will attempt to read the {file_name} file.")
    input("Press ENTER to continue >>>")

    try:
        with open(file_name, "r") as f: 
            content = f.readlines()
            content = [int(x) for x in re.findall(r"(?<!\.)\b\d+\b(?!\.)", str(content))]
        f.close()

        return content

    except FileNotFoundError as FNFE:
        print(f"Error while accessing the file {file_name}: {FNFE}") 
        raise FileNotFoundError
    except IOError as IOE: 
        print(f"Error while accessing the file {file_name}: {IOE}") 


def write_file(output):

    print(output)

    try:
        with open('output.txt', 'w') as f: 

            # numerical complexity = O(n); auxiliary space = O(1); 
            output = ','.join([str(elem) for elem in output])
            f.write(output.replace("(", "[").replace(")", "]"))
        f.close()
        print(f"The following pairs were found and saved in the output.txt file: {output}")

    except IOError:
        print("Error while creating the file output.txt")
    except TypeError:
        print("No elements were found.")


if __name__ == "__main__":
    input = open_file("input.txt")
    output = find_pairs(input)
    write_file(output)