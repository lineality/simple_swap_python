# "Easy things are hard." -> 'Problem 12= Flip 1 and 2 in "1+2=3" in this sentence.'

import hashlib
import random

# helper function
def print_and_log(message, log_name):
    # Print the message to the console
    print(repr(message))
    print(message)

    # Append the message to the specified log file
    with open(log_name, 'a') as log_file:
        log_file.write(repr(message) + '\n')


# Helper Function
def string_get_seed_from_sha256_hash(input_string, log_name):
    """
    turn input_string into a sha256 hash
    to use a seed to randomly but repeatably
    """

    # start hash
    string_hash = hashlib.sha256()

    # remove escape characters
    input_string = input_string.replace("\\", "")

    # remove escape ch
    # aracters
    input_string = input_string.replace("\\\\", "")

    print_and_log(f"input string for seed: {input_string}", log_name)

    # hash the string
    string_hash.update(input_string.encode('utf-8'))

    # make the hash an int not hex
    string_hash = string_hash.hexdigest()

    print_and_log(f"hash for seed: {string_hash}", log_name)

    return string_hash


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
        print(f"NOTHING DONE: item to match not in string -> {item_1} vs. {input_string}")
        return input_string

    use_this_placeholder = ';;;<<<'

    """all possible ascii placeholders, and more:
    while there is a risk of item 1 or two coliding with the placeholder
    there is also a risk of the placeholder coliding with part of the string
    the longer the string, the more likely it contains any given single
    ascii character 
    """
    placeholder_list = [
        '!!!"""', '###$$$', '%&%&%&', "'''(((", ')))***', 
        '+++,,,', '---...', '///000', '111222', '333444', 
        '555666', '777888', '999:::', ';;;<<<', '===>>>', 
        '???@@@', 'AAABBB', 'CCCDDD', 'EEEFFF', 'GGGHHH', 
        'IIIJJJ', 'KKKLLL', 'MMMNNN', 'OOOPPP', 'QQQRRR', 
        'SSSTTT', 'UUUVVV', 'WWWXXX', 'YYYZZZ', '[[[sss', 
        ']]]^^^', '___```', 'aaabbb', 'cccddd', 'eeefff', 
        'ggghhh', 'iiijjj', 'kkklll', 'mmmnnn', 'oooppp', 
        'qqqrrr', 'sssttt', 'uuuvvv', 'wwwxxx', 'yyyzzz', 
        '{|{{|||', '}~}~}~~~',
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


# helper function
def apply_swap(input_string, log_name, error_description, item_1, item_2):
    """
    requires: 
        import hashlib
        import random
    
    requires/uses helper functions:
        print_and_log(message, log_name)
        string_get_seed_from_sha256_hash(input_string, 1)
        swap_two(selected_segment, item_1, item_2)
      
    This function: 
    input parameters: apply_swap(input_string, log_name, error_description, item_1, item_2)
      
    apply_swap() function logs and applies a swap
    to an equation, deterministically-randomly to some segment of the equation,
    where the item is found,

    It checks for indices where both match
    or where at least one matches
    or where none match
    and deterministically-randomly selects from those.
    
    produces a cumulative description of changes made 'error_description' (string)
    and appends to a cumulative log file-document: file-path->log_name
    """

    print_and_log(f"start apply_swap({input_string}, log_name, {item_1}, {item_2})", log_name)

    if item_1 not in input_string:
        print_and_log(f"no match: {item_1} -> {input_string} ", log_name)
        return input_string, error_description

    # step 1: input original string and potentially two items to change in it
    original_equation = input_string

    # Step 2: Split string on "="
    list_of_splits = input_string.split("=")

    print_and_log(f"Initial list_of_splits: {list_of_splits}", log_name)

    # Step 3: Randomly pick one split using string_get_seed_from_sha256_hash() for random seed
    """
    have the input to see include more than just the equation,
    or every change may similarly be made to the same segment
    """
    input_to_seed = input_string + item_1 + item_2
    seed = string_get_seed_from_sha256_hash(input_to_seed, log_name)
    random.seed(seed)
    # log
    print_and_log(seed, log_name)

    # pick a random item-index in list WHERE the item is found.
    """
    Return a list of indices from `list_of_splits` where the string contains 
    ideally both `item_1` and `item_2`, if not that
    item_1
    """
    filtered_indices = [index for index, s in enumerate(list_of_splits) if item_1 in s and item_2 in s]
    if not filtered_indices:
        filtered_indices = [index for index, s in enumerate(list_of_splits) if item_1 in s]

    # check length:
    if not filtered_indices:
        print_and_log(f"no match: {input_string} {item_1}", log_name)
        return input_string

    # select randomly from optional indices where fine items are found
    chosen_split_index = random.choice(filtered_indices)

    # log
    print_and_log(f"chosen_split_index: {chosen_split_index}", log_name)

    # Step 4: Make a change in only that one split picked
    selected_segment = list_of_splits[chosen_split_index]
    # apply
    modified_split = swap_two(selected_segment, item_1, item_2)
    # log
    print_and_log(f"modified_split: {modified_split}", log_name)

    # Replace the chosen split with the modified one
    list_of_splits[chosen_split_index] = modified_split

    # Step 5: Re-combine list_of_splits
    result_string = "=".join(list_of_splits)


    ###################
    # Log Changes Made
    ###################

    if item_1 in original_equation:
        message = f"Changed {item_1} to {item_2}"
        print_and_log(message, log_name)
        error_description += message + "; "

    if item_2 in original_equation:
        message = f"Changed {item_2} to {item_1}"
        print_and_log(message, log_name)
        error_description += message + "; "

    # log
    print_and_log(f"Final string: {result_string}", log_name)

    message = f"""
    Final equation comarison:
    old -> {original_equation}
    new -> {result_string}
    """
    print_and_log(message, log_name)

    # Step 6: Return string
    return result_string, error_description


##############
# example run
##############
log_name = "log.txt"
error_description = "So far..."
# apply_swap(input_string, log_name, error_description, item_1, item_2)
result = apply_swap("applebanana=cherrybanana=cherrybanana", log_name, error_description, "a", "b")

print(f"Result: {result}")
