'''
PAPER DOLL: Given a string, return a string where for every character in the original 
there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(text):
    new_word = ""
    for letter in text:
        new_word += letter*3
    return new_word

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))



