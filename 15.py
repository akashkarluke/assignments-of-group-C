# Question No:15 -Python | Ways to check if element exists in list
list = ["akki","ak12#",234,0,1,9,"puja",12.89,18.19,"12ak@A",7,"akki"]
print(list)

#way 1(naive method)

# if 2342 in list:
#     print("yes present")
# else:
#     print("no not present")
#
#     if "ak12#" in list:
#         print(True)
#     else:
#         print(False)

#way 2

# print(18.19 in list)
# print("pooja" in list)
# print("akash" not in list)

#way 3

# if list.count("akki") > 0:
#    print(True)
# else:
#     print(False)

#way 4(using loop)

# for i in list:
#     if i == "akaksh":
#         print("element exist")
#
#     #else:
#         #print("not exist")


#way 5 (using loop + break)
# if i == "akki":
#     print("element exist")
#     break
# else:
#     print("not exist")


#way 6 (using not in + append)

# for i in list:
#     if "karluke" not in list:
#         list.append("karluke")
#         print(list)


print('kya kar rahe ho')