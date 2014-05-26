import sys
from collections import Counter

if (len(sys.argv[1]) >20):
    print("word needs to be less than 20 characters")
    exit()
else:
    word = sys.argv[1]


def calculate_rank(word):
    rank = 1
    suffix = 1
    counter = Counter()
    for i in range(len(word)):
        #reverse the word
        x = word[((len(word) - 1) - i)]
        counter[x] += 1
        for y in counter:
            if (y < x):
                rank += ((suffix * counter[y]) // counter[x])
        suffix = ((suffix * (i + 1)) // counter[x]) 
    return rank
       

def main():

    print(calculate_rank(word))

if __name__ == '__main__':
    main()
