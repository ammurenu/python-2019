'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''

def master_yoda(text):
    word_list = text.split()
    reverse_word_list = word_list[::-1]
    return ' '.join(reverse_word_list)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))


