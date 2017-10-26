#!/usr/bin/env python3

# Assignment 3: Bank

# matress object, consiting of bag objects
class Matress():
    def __init__(self):
        self.bags = []
    # adds bag from object
    def add(self, bag):
        self.bags.append(bag)
    # removes bag from object
    def remove(self, bag):
        self.bags.remove(bag)
    # returns value of all bags objects
    def networth(self):
        if self.bags:
            running_total = 0.00
            for each_bag in self.bags:
                running_total += each_bag.bag_value()
            return running_total
        else:
            return 0.00

# bag object
class Bag():
    def __init__(self, name, quarters, dimes, nickels, pennies, edit=True):
        self.name = name
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies
        self.edit = edit
    # returns bag value of coins
    def bag_value(self):
        return 0.25*self.quarters + 0.10*self.dimes + 0.05*self. nickels + 0.01*self.pennies
    # transfers coins to bag from another bag
    def transfer(self, bag_from):
        self.quarters = self.quarters + bag_from.quarters
        self.dimes = self.dimes + bag_from.dimes
        self.nickels = self.nickels + bag_from.nickels
        self.pennies = self.pennies + bag_from.pennies
    # converts coins to text output
    def text_value(self):
        text_list = []
        if self.quarters == 1:
            text_list.append( str(self.quarters)+" quarter")
        elif self.quarters > 1:
            text_list.append( str(self.quarters)+" quarters")
        if self.dimes == 1:
            text_list.append( str(self.dimes)+" dime")
        elif self.dimes > 1:
            text_list.append( str(self.dimes)+" dimes")
        if self.nickels == 1:
            text_list.append( str(self.nickels)+" nickel")
        elif self.nickels > 1:
            text_list.append( str(self.nickels)+" nickels")
        if self.pennies == 1:
            text_list.append( str(self.pennies)+" penny")
        elif self.pennies > 1:
            text_list.append( str(self.pennies)+" pennies")
        if len(text_list) > 1:
            text_list.insert( len(text_list)-1 ,"and" )
        string_text_1 = str( text_list )[2:-2]
        string_text_2 = string_text_1.replace("'","")
        if text_list:
            if len(text_list) == 3:
                string_text_3 = string_text_2.replace(",","")
                return string_text_3
            else:
                string_text_4 = string_text_2.replace("and,","and")
                return string_text_4
        else:
            return "nothing"

# main menu function for each loop
def menu():
    print("Please choose an option (1-5):")
    print("1) Balance Inquiry")
    print("2) Deposit")
    print("3) Transfer")
    print("4) Withdrawl")
    print("5) Flee the Country!\n")
    user_input = input("> ")
    while True:
        if user_input not in ['1','2','3','4','5']:
            print("\n***ERROR*** invalid input, please try again...\n")
            user_input = input("> ")
            continue
        else:
            break
    return user_input

# main program: initial conditions
bank = Matress()
bugout_bag = Bag("Bugout Bag",0,0,0,0)
bank.add(bugout_bag)
unique_bag_number_name = 1
print("\nWelcome to Erste Bank der Matratze\n")

# main program loop
while True:

    # display menu
    user_input = menu()

    # balance inquiry
    if user_input == '1':
        if bank.bags:
            # sort bags by value, with bugout bag at top
            bag_list_to_sort = []
            for each_bag in bank.bags:
                bag_list_to_sort.append(each_bag)
            sorted_list = sorted(bag_list_to_sort, key=lambda x:x.bag_value(), reverse=False)
            for each_bag in sorted_list:
                if each_bag.name == "Bugout Bag":
                    sorted_list.insert(0,sorted_list.pop(sorted_list.index(each_bag)))
            # print bag values in order
            print("")
            for each_bag in sorted_list:
                string_temp_1 = each_bag.name+":"
                string_temp_2 = "$"+format(each_bag.bag_value(),'.2f')
                string_print = '{:<20} {:>20}'.format(string_temp_1, string_temp_2)
                print(string_print)
        # print total
        string_temp_1 = "Total:"
        string_temp_2 = "$"+format(bank.networth(),'.2f')
        print("-----------------------------------------")
        string_print = '{:<20} {:>20}'.format(string_temp_1, string_temp_2)
        print(string_print,"\n")
    # deposit
    elif user_input == '2':
        # get bag name input from user
        name = input("\nEnter name of deposited bag: ")
        name = name.strip()
        # check if unique name, if not, assign unique value name
        bag_name_list = []
        for each_bag in bank.bags:
            bag_name_list.append(each_bag.name)
        if name in bag_name_list:
            print("\n***ERROR*** Duplicate bag name detected!")
            print("NOTE: Unique bag number",unique_bag_number_name,"automatically assigned\n")
            name = str(unique_bag_number_name)
            unique_bag_number_name += 1
        # no name, assign unique value name
        elif name == "":
            print("NOTE: Unique bag number",unique_bag_number_name,"automatically assigned")
            name = str(unique_bag_number_name)
            unique_bag_number_name += 1
        # get coin input from user
        coins = input("Enter number of quarters, dimes, nickels, and pennies (# # # #): ")
        coins_list = coins.split()
        user_closed = input("Stitch bag closed (yes/no)? ")
        if user_closed in ['yes','y','YES','Yes','Y']:
            print("Bag stitched closed! You can't edit it anymore!")
            edit = False
        else:
            edit = True
        # confirm valid input
        if len( coins_list ) == 4:
            if coins_list[0].isdigit() and coins_list[1].isdigit() and coins_list[2].isdigit() and coins_list[3].isdigit():
                quarters = int( coins_list[0] )
                dimes = int( coins_list[1] )
                nickels = int( coins_list[2] )
                pennies = int( coins_list[3] )
                new_bag = Bag(name, quarters, dimes, nickels, pennies, edit)
                bank.add(new_bag)
                print("\nBag Deposited!\n")
        # invalid input error
        else:
            print("\n***ERROR*** Unable to determine number of coins!")
            print("Bag not deposited!\n")

    # trasnfer
    elif user_input == '3':
        # user input
        bag_from = input("\nEnter the name of the bag to transfer from: ")
        bag_into = input("Enter the name of the bag to transfer into: ")
        # check inputs
        bag_name_list = []
        for each_bag in bank.bags:
            bag_name_list.append(each_bag.name)
        # invalid bag names
        if (bag_from not in bag_name_list):
            print("\n***ERROR*** Could not withdraw a bag with that name!\n")
        elif (bag_into not in bag_name_list):
            print("\n***ERROR*** Could not transfer into a bag with that name!\n")
        # transfer between bags
        else:
            for find_from_bag in bank.bags:
                for find_into_bag in bank.bags:
                    if find_from_bag.name == bag_from:
                        if find_into_bag.name == bag_into:
                            if (find_from_bag.edit == False):
                                print("\n***ERROR*** Could not open source bag, it is stitched closed!\n")
                            elif (find_into_bag.edit == False):
                                print("\n***ERROR*** Could not open destination bag, it is stitched closed!\n")
                            else:
                                find_into_bag.transfer(find_from_bag)
                                print("\n$"+format(find_from_bag.bag_value(),".2f"),"transfered!\n")
                                bank.remove(find_from_bag)

    # withdrawal
    elif user_input == '4':
        # user input
        bag_to_remove = input("\nEnter the name of the bag you want to withdrawal: ")
        # search for user input bag name
        bag_name_list = []
        for each_bag in bank.bags:
            bag_name_list.append(each_bag.name)
        # invalid bag name errors
        if bag_to_remove not in bag_name_list:
            print("\n***ERROR*** Could not withdraw a bag with that name!\n")
        elif bag_to_remove == "Bugout Bag":
            print("\n***ERROR*** Can not remove Bugout Bag, you must flee the country!\n")
        # remove bag
        else:
            for each_bag in bank.bags:
                if each_bag.name == bag_to_remove:
                    print("\nYou withdrew "+each_bag.text_value()+".\n")
                    bank.remove(each_bag)

    # flee country 
    else:
        # print total left behind
        string_temp_1 = "\nYou have fled the country, leaving $"
        total_less_bugout = bank.networth() - bugout_bag.bag_value()
        string_temp_2 = format(total_less_bugout,".2f")
        print(string_temp_1 + string_temp_2 + " behind!")
        # display coins removed
        print("You took "+bugout_bag.text_value()+" with you.\n")
        break
