
from collections import Counter
#list1 = ['x','y','z','x','x','x','y', 'z']
#print(Counter(list1))



def largest_anagram(string):
    # split input string separated by space
    string = string.split(" ")

    # sort each string in given list of strings
    for i in range(0, len(string)):
        string[i] = ''.join(sorted(string[i]))

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    Dict = Counter(string)

    # get maximum value of frequency
    print(max(Dict.values()))


# Driver program
if __name__ == "__main__":
    string = 'post, pots, spot, stop, tops, alerts, alters, salter ant magenta magnate tan gnamate'

largest_anagram(string)

