# simple_swap_python

```
import sys

# helper_function
def swap_two(input_string, item_1, item_2):
    """
    Swap two items in a string. Tada!

    or change only the first item, the 2nd item is optional.

    protection from swap-collisions is included
    """

    original_string = input_string

    # validity sanity check (item_2 is optional, only item 1 is needed)
    if item_1 not in input_string:
        print(f"item to match not in string -> {item_1} vs. {input_string}")
        sys.exit()

    use_this_placeholder = ';;;<<<'

    """all possible ascii placeholders, and more:
    while there is a risk of item 1 or two coliding with the placeholder
    there is also a risk of the placeholder coliding with part of the string
    the longer the string, the more likely it contains any given single
    ascii character 
    """
    placeholder_list = [
        '!!!"""', '###$$$', '%%%&&&', "'''(((", ')))***', 
        '+++,,,', '---...', '///000', '111222', '333444', 
        '555666', '777888', '999:::', ';;;<<<', '===>>>', 
        '???@@@', 'AAABBB', 'CCCDDD', 'EEEFFF', 'GGGHHH', 
        'IIIJJJ', 'KKKLLL', 'MMMNNN', 'OOOPPP', 'QQQRRR', 
        'SSSTTT', 'UUUVVV', 'WWWXXX', 'YYYZZZ', '[[[sss', 
        ']]]^^^', '___```', 'aaabbb', 'cccddd', 'eeefff', 
        'ggghhh', 'iiijjj', 'kkklll', 'mmmnnn', 'oooppp', 
        'qqqrrr', 'sssttt', 'uuuvvv', 'wwwxxx', 'yyyzzz', 
        '{{{|||', '}}}~~~',
        '!', '"', '#', '$', '%', '&', "'", '(', 
        ')', '*', '+', ',', '-', '.', '/', '0', '1', 
        '2', '3', '4', '5', '6', '7', '8', '9', ':', 
        ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 
        'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', 
        '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
        'z', '{', '|', '}', '~', 
    ]

    """
    check that:
    item_2 is not in placeholder
    that placeholder does not collide with something in string
    """
    placeholder_ok = False
    for this_placeholder in placeholder_list:
        print(f"trying -> '{this_placeholder}'")
        if (item_1 not in this_placeholder) and (item_2 not in this_placeholder) and (this_placeholder not in input_string):
            use_this_placeholder = this_placeholder
            placeholder_ok = True
            print(f"use_this_placeholder -> {use_this_placeholder}")
            break
        else:
            print("collision detected, try next placeholder...")

    if not placeholder_ok:
        # print error message and exit program
        message = """FAILED: collision error, 
        for swap_two(), 
        a new placeholder needed. 
        action item: add novel option to placeholder_list
        """
        print(message)
        sys.exit()


    # Replace item_1 with a temporary placeholder
    output_swapped_string = input_string.replace(item_1, use_this_placeholder)
    print(output_swapped_string)

    # Replace item_2 with item_1
    output_swapped_string = output_swapped_string.replace(item_2, item_1)
    print(output_swapped_string)

    # Replace that temporary placeholder with item_2 (done and done)
    output_swapped_string = output_swapped_string.replace(use_this_placeholder, item_2)

    message = f"""
    Final comarison:
    old -> {original_string}
    new -> {output_swapped_string}
    """
    print(message)

    return output_swapped_string


```
