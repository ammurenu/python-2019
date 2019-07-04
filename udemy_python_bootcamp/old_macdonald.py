'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
'''

def old_macdonald(name):
    new_word = ""
    for index,letter in enumerate(name):
        if index == 0 or index == 3:
            letter = letter.upper()
        new_word += letter
    return new_word

print(old_macdonald('macdonald'))

