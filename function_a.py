from statistics import mode


def most_common_value(number_list):
    """ returns the most common element of the list
    """
    most_common = mode(number_list)
    return most_common

def second_element(numbers_list):

    return True #Poppy try to make a merge conflict here

if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
