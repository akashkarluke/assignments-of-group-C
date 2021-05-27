#Python program to count the frequency of elements in a list using a dictionary

#list[1,2,4,5,3,5,1,2,3,4,5,1,1,1,2,2,2,5]

def freq_elemnts(list1):
    dict = {}
    for items in list1:
        dict[items] = list1.count(items)

    for key, value in dict.items():
        print(key, value) #("% d : % d"%)
if __name__ == '__main__':
    list1 = ["akki","akki","akash","puja","amol", "akash","akki","puja","puja"]
    #list1 = [1,2,3,1,2,3,4,5,4,5,4,5,4,2,3,2,1,2,2,3,2,3,1,2,3,3,4,4,2,5,5]
    #list1 = input("enter the number/string:- ")


freq_elemnts(list1)
