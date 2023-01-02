from random import sample
from math import factorial


def Combination_Calculator(given_list: list,
                           group_size: int) -> list:
    """
    Consumes a list of str and an int and returns all possible combinations without any
    repeating elements of the given_list in groups of group_size. Assumes that 123 = 321 = 213 = ... etc,
    and cat-dog-bird = dog-bird-cat = ... etc.

    requires:
        given_list > group_size > 0

    :rtype: list
    :param given_list:
    :param group_size:
    :return combinations:
    """

    combinations = [ ]  # list of groupings

    # the total number of groupings there should be ie the length combinations should get to

    if group_size > len (given_list):
        print (f"Error: group size must be <= {len (given_list)}")
    else:
        end = (factorial (len (given_list)) / (factorial (group_size)
                                               * factorial ((len (given_list) - group_size))))
        while len (combinations) <= end - 1:
            # grabbing group-size # of random elements from the given_list
            ls = sample (given_list, group_size)
            group = ''.join (sorted (ls))
            if group in combinations:  # checking if these elements are already in combinations
                continue
            combinations.append (group)
        print (f'there are {end} possible combinations:')
        print (" ".join (sorted (combinations)))
        return sorted (combinations)


lst = input ("input some stuff with spaces separating individual things: ").split ()
grouping = int (input ("input a number for the size of each grouping: "))

print (f'list: {lst} \n group-size: {grouping}')

Combination_Calculator (lst, grouping)