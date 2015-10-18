from collections import Counter
import matplotlib.pyplot as plt

data = {}
documentName = raw_input('Please Enter the Document Name: ')
documentContent = []
documentHandle = open(documentName)

for x in documentHandle.read():
    documentContent.append(x)
# We remove punctuation marks:
documentContent = " ".join(c for c in documentContent if c not in (',','.','?',':',';'))

# We remove spaces also:
documentContent.replace(" ","")

# Separate the words into letters and count
#documentContent = [x for x in set(documentContent)]

lettersOfAlphabet = [x for x in set('abcdefghijklmnopqrstuvwxyz')]

# create an array to store the number of occurence of each letter in
# the alphabet
for x in lettersOfAlphabet:
    data.update({x:documentContent.count(x)})

plt.bar(range(len(data)),data.values(),align='center')
plt.xticks(range(len(data)),data.keys())
plt.xlabel('Letters of the Alphabet')
plt.ylabel('Number of Occurence')
plt.title('Bar Graph showing the number of occurence of letters \n of the alphabet in a text')
plt.show()




