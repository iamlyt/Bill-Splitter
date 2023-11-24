import random

print("Enter the number of friends joining (including you):")
num_of_friends = int(input())
# original dict
friends_joining = dict()

if num_of_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")

    # add key and default values to friends_joining dictionary
    for _ in range(num_of_friends):
        name = input()
        friends_joining[name] = 0

    # ask for total bill then split it -- round 2 decimal places
    print("\nEnter the total bill value:")
    bill_value = int(input())
    split_amount = round(bill_value / num_of_friends, 2)

    # update keys with corresponding values
    for key in friends_joining:
        friends_joining[key] = split_amount

    # ask if they want to use lucky feature
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature = input()

    if lucky_feature == "Yes":
        # generate random name from list of keys
        names_list = [*friends_joining.keys()]
        lucky_name = random.choice(names_list)
        print(f"\n{lucky_name} is the lucky one!")

        # new split values
        split_amount = round(bill_value / (num_of_friends - 1), 2)

        # create a new dictionary here with the new split values
        new_dict = {key: split_amount for (key, value) in friends_joining.items()}
        # lucky_name pays 0
        new_dict[lucky_name] = 0

        print(new_dict)
    else:
        print(f"\nNo one is going to be lucky\n{friends_joining}")


