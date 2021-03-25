from bs4 import BeautifulSoup

# open paula choice dictionary html document (view-source file)
with open("pd.htm") as fp:
    soup = BeautifulSoup(fp,"html.parser")

# ordered list means 1st element of ingredient name corresponds to
# 1st element of category list and 1st element of ratings list, and so on

# find all ingredient titles that are enclosed with h2 class tags
h2_tag = soup.find_all("h2", "name ingredient-name")
# create ordered list of ingredient names
ingredients_name = []
for each in h2_tag:
    name = each.a.contents[0] # extract name within <a href>...</a>
    name = name.lower() # change name to lowercase
    ingredients_name.append(name) # add to ordered list

# find ingredient categories enclosed in div tags
div_tag = soup.find_all("div", "categories ingredient-categories")
# create ordered list of categories
category_list = []
for each in div_tag:
    types = each.find_all("a") # some ingredients have more than 1 categories
    # the above line serves to find the categories with <a href> tags
    category = []
    for ii in range(len(types)):
        category.append(types[ii].contents[0]) # extract category name 
    category_list.append(category) # add to ordered category list

# find ratings enclosed in td tags that have class "col-rating..."
td_tag = soup.find_all("td", "col-rating") 
# create ordered list of rating of ingredient
ratings_list = []
for each in td_tag:
    ratings_list.append(each.contents[0]) # extract rating from <a href>...</a>

# create dictionary of ingredients
dictionary = {}
for ii in range(len(ingredients_name)):
    name = ingredients_name[ii]
    category = category_list[ii]
    rating = ratings_list[ii]
    dictionary[name] = {}
    dictionary[name]["Category"] = category
    dictionary[name]["Rating"] = rating









