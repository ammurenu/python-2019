def file_extraction(file_name):
    file_content = {}
    content = open(file_name,'r')
    for index,line in enumerate(content):
        file_content[index+1] = line.split()
    return file_content

def recipe_selection(file_content,recipe_index):
    return file_content[recipe_index][0]
            


file_content = file_extraction('recipe.txt')
print('Recipe List \n {fc}'.format(fc = file_content))
recipe_index = input('Enter your recipe selection number: ')

recipe = recipe_selection(file_content,recipe_index)
print(recipe)

print(recipe.split(','))

