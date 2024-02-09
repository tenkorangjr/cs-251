'''csv_reader.py
Reads in data from .csv files
Michael Tenkorang
CS 251: Data Analysis and Visualization
Lab 1a
'''
from typing import List, Dict

def read_csv(filepath):
    '''Reads and returns the data from a CSV file located at `filepath`.

    Parameters:
    -----------
    filepath: str. Path to the .csv file to be read in.

    Returns:
    -----------
    List of lists. The data loaded from the .csv file.

    ----------------------------------------------------------------------------
    Example:
    For a .csv file that looks like:

    a,b,c
    1,2,3

    The corresponding list of lists that this function should return looks like:
    [[a, b, c], [1, 2, 3]]
    ----------------------------------------------------------------------------

    TODO:
    Write code below that does what the docstring above states (i.e. read in the .csv file, organize the data as a
    list of lists, return the list of lists).

    NOTE:
    - You should only use standard Python to implement this method. Do not import other modules.
    - Remember that Python has a helpful `split` string method that splits up a string into a list based on a delimitter
    of your choice.
    - There is a helpful string method to remove new line characters.
    - If you are not using a `with` block, don't forget to close the file handle!
    '''
    # YOUR CODE HERE (you can delete the pass statement below)
    
    with open(filepath, 'r') as data_file:
        contents: List[str] = data_file.readlines()

        data: List[List[str]] = []
        for row in contents:
            inner_data_list: List[str] = row.split(",")

            cur: List[str] = []
            for item in inner_data_list:
                if item:
                    cur.append(item.strip())
                else:
                    cur.append("missing")

            data.append(cur)
        
    return data


def read_cat_csv(filepath):
    '''Reads in a CSV file containing categorical data located at `filepath`. Codes the imported categorical data using
    ints (0, 1, ...).

    Parameters:
    -----------
    filepath: str. Path to the .csv file to be read in.

    Returns:
    -----------
    List of lists. The data loaded from the .csv file. ONLY contains ints. The ints represent each variables categorical
        levels coded as ints rather than strings.
    Dictionary. The dictionary that contains the mappings between categorical variable names (keys) and the corresponding
        list of unique levels (represented as STRINGS) of each categorical variable (values).

    ----------------------------------------------------------------------------
    Example:
    For a .csv file that looks like:

    a,1,hi
    b,2,hi
    c,2,hi

    The corresponding list of lists that this function should return looks like:
    [[0, 1, 2], [0, 1, 1], [0, 0, 0]]
    and the dictionary should look like (key -> value)
    'var1' -> ['a', 'b', 'c']
    'var2' -> ['1', '2']
    'var3' -> ['hi']
    ----------------------------------------------------------------------------

    TODO:
    Write code below that achieves what the docstring above states.

    NOTE:
    - Assume that the 3 categorical variables in categorical.csv are called and hard-coded as 'name', 'year', 'hobby'.
    We are doing this because the CSV files in today's lab do not have header or types rows. Use these keys in your
    dictionary.
    - You should only use standard Python to implement this method. Do not import other modules.
    - Your code from `read_csv` above should be a helpful starting point.
    - Reviewing your code in dictionary_practice.py should also be helpful.
    '''
    # KEEP ME
    # Names of the variables in categorical.csv in the correct order
    var_names = ['name', 'year', 'hobby']

    # YOUR CODE HERE
    # Initialize level dictionary to empty lists...
    cat_to_levels: Dict[str, List[str]] = {var_names[i]: [] for i in range(len(var_names))}

    list_from_read_csv: List[List[str]] = read_csv(filepath = filepath)

    output_data: List[List[int]] = []
    for line in list_from_read_csv:
        inner_data_list: List[int] = []

        for data_idx in range(len(line)):
            # check dictionary to see if the data exists in the value (an array) of its header
            data: str = line[data_idx]
            cat_to_levels_value: List[str] = cat_to_levels[var_names[data_idx]]
            if data not in cat_to_levels_value:
                cat_to_levels_value.append(data)
                inner_data_list.append(len(cat_to_levels_value) - 1) # add the last index of the list
            else:
                inner_data_list.append(cat_to_levels_value.index(data))

        output_data.append(inner_data_list)

    return output_data, cat_to_levels


    
