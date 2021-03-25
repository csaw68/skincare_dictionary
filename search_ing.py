import pprint

from pc_d import dictionary

def search():
    # list for ingredients not found
    not_found = []

    # lists for different ratings of ingredients
    best = []
    good = []
    average = []
    poor = []

    print("This program takes in information from Paula's Choice Skincare Dictionary.")
    # get user input for ingredients list
    string = input("Copy and paste ingredients below: (enter 0 to quit) \n")
    if string == '0':
        print("End of program")
        return ""
    # separate string into list elements by commas
    ing_list = string.split(",")
    print("\nCategory and Quality of Ingredients\n")
    
    for ii in range(len(ing_list)):

        # clean up ingredients string
        ingredient = ing_list[ii]
        ingredient = ingredient.strip()
        ingredient = ingredient.strip(".")
        
        if ingredient.lower() in dictionary.keys():
            # print name of ingredient
            print(ingredient)
            # print returned values of ingredient found in dictionary
            pprint.pprint(dictionary[ingredient.lower()])
            # categorize ingredients quality by their ratings
            if dictionary[ingredient.lower()]['Rating'] == 'Best':
                best.append(ingredient)
            elif dictionary[ingredient.lower()]['Rating'] == 'Good':
                good.append(ingredient)
            elif dictionary[ingredient.lower()]['Rating'] == 'Average':
                average.append(ingredient)
            elif dictionary[ingredient.lower()]['Rating'] == 'Poor': 
                poor.append(ingredient)                
            print('\n')
            
        else:
            # add ingredient to not_found list if not found in dictionary
            not_found.append(ingredient)

    print("Total Number of Ingredients:",len(ing_list))

    # only print quality lists if there are elements in them
    if bool(best) == True:
        print("\nBest Ingredients:")
        pprint.pprint(best)
    if bool(good) == True:
        print("\nGood Ingredients:")
        pprint.pprint(good)
    if bool(average) == True:
        print("\nAverage Ingredients:")
        pprint.pprint(average)
    if bool(poor) == True:
        print("\nPoor Ingredients:")
        pprint.pprint(poor)

    # print ingredients not found within dictionary
    print("\nList of Ingredients Not Found:")
    pprint.pprint(not_found)

    print('\n')
    search()
