#4) Write a program that counts the occurances of each word in a given sentence.
#  Example for the sentence "hello world hello", the output should be {'hello':2, 'world' : 1}.
def word_count(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict
sentence = "hello world hello"
word_counts = word_count(sentence)
print(word_counts) 