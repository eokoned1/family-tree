"""
File:    family_tree.py
Author:  Mofe Okonedo
E-mail:  eokoned1@umbc.edu
Description:
Family Tree
"""


def create(name):
    if name not in people:
        people[name] = {'mother': 'None', 'father': 'None', 'children': []}
        print(f'{name} has been created.')
    else:
        print(f"{name} already exists")


# creates a new person with a name, if the person already exists, then it doesn't make a new person and states the
# person already is there


def get_input(user_input):
    split_input = user_input.split()  # splitting the input into list, so we can use if statements to use our functions
    if split_input[0] == 'create':
        create(split_input[1])
    elif split_input[0] == 'set-mother':
        set_mother(split_input[1], split_input[2])
    elif split_input[0] == 'set-father':
        set_father(split_input[1], split_input[2])
    elif split_input[0] == 'is-ancestor':
        ancestor_check, no = is_ancestor(split_input[1], split_input[2])
        print(ancestor_check)
    elif split_input[0] == 'is-descendant':
        descendant_check, _ = is_descendant(split_input[1], split_input[2])
        print(descendant_check)
    elif split_input[0] == 'display_person':
        display_person(split_input[1])
    elif split_input[0] == 'display-people':
        display_people()
    elif split_input[0] == 'save':
        save(split_input[1])
    elif split_input[0] == 'load':
        load(split_input[1])


def set_mother(name, mother_name):
    if name in people:  # uses for loop to go through the dictionary that is people
        if people[name]['mother'] == "None":
            if mother_name in people:
                people[name]['mother'] = mother_name  # sets mother of person with the name to the given mother name
                people[mother_name]['children'].append(name)
        else:
            print(f"{name} already has a mother")  # else print they already have a mother
    else:
        print(f"{name} does not exist")  # if they aren't in the tree, prompt that they don't exist


def set_father(name, father_name):
    if name in people:  # same as set_mother loops through the dictionary
        if people[name]['father'] == "None":
            if father_name in people:
                people[name]['father'] = father_name  # sets father of person with the name to the given father name
                people[father_name]['children'].append(name)
        else:
            print(f"{name} already has a father")  # else print they have a father
    else:
        print(f"{name} does not exist")


def is_ancestor(ancestor_name, person_name, depth=0):  # checks if the person with this ancestor name is an ancestor
    # of the person_name parameter
    if ancestor_name == person_name:
        return True, depth
    if not people[person_name]['mother']:
        result, new_depth = is_ancestor(ancestor_name, people[person_name]['mother'], depth + 1)  # recursive call
        # with default functions
        if result:
            return True, new_depth
    if not people[person_name]['father']:
        result, new_depth = is_ancestor(ancestor_name, people[person_name]['father'], depth + 1)  # recursive call
        if result:
            return True, new_depth
    return f'{ancestor_name} is not an ancestor of {person_name}', -1


def is_descendant(descendant_name, person_name, depth=0):  # checks if a person with the descendant name is a
    # descendant of the person with the name in person_name
    if descendant_name == person_name:
        return True, depth
    if not people[person_name]['children']:
        return f'{descendant_name} is not a descendant of {person_name}', -1
    for child in people[person_name]['children']:
        result, new_depth = is_descendant(descendant_name, child, depth + 1)
        if result:
            return True, new_depth
    # print(f'{descendant_name} is not a descendant of {person_name}')
    return False, -1


def display_person(name):  # the function loops through the dictionary of people and uses if statements to print the
    # people in the family tree or not
    if name in people:
        print(f"{name}")
        if people[name]['mother']:
            print(f"  Mother: {people[name]['mother']}")
        if people[name]['father']:
            print(f"  Father: {people[name]['father']}")
        if people[name]['children']:
            print("  Children:")
            for child in people[name]['children']:
                print(f"    {child}")
    else:
        print(f"{name} does not exist")


def display_people():  # recursively displays the people who are in the family tree
    for person in people:  # loops through the dictionary
        display_person(person)  # recursive calls


def save(filename):
    with open(filename, 'w') as file:  # opens the file then write in it
        for person in people:
            mother = people[person]['mother'] if people[person]['mother'] else "None"
            father = people[person]['father'] if people[person]['father'] else "None"
            file.write(f"{person}:{mother}:{father}\n")  # one person per line


def load(filename):
    with open(filename, 'r') as file: # open then read the file
        for line in file:
            # split the line into name, mother, father, and children
            name, mother, father = line.strip().split(":")
            create(name)
            if mother != 'None':
                set_mother(name, mother) # call set_mother function
            else:
                set_mother(name, 'None')
            if father != 'None':
                set_father(name, father)
            else:
                set_father(name, 'None')


if __name__ == '__main__':  # main function
    people = {} # main family tree dictionary
    the_input = input('>> ')
    while the_input != "exit": # while the input is not equal to exit prompt the input again
        get_input(the_input)
        the_input = input('>> ')
