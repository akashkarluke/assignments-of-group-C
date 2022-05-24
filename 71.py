#Python dictionary, set and counter to check if frequencies can become same

from collections import Counter
def samefreq(input):
     dict = Counter(input)
     temp = list(set(dict.values()))
     if len(temp) > 2:
         print("NO")
     elif len(temp) == 2 and (temp[1]) - (temp[0]) > 1:
         print("NO")
     else:
         print("YES")

if __name__ == '__main__':
    input  = "xxxxyyzz"

samefreq(input)


print('hi verendra')
