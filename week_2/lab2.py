#exercise 1
list = []
list= input("enter list of num:").split()
rev= list[::-1]
print(rev)

#exercise 2

list2 =[(x**2) for x in range (21) if x%2 ==0]
print(list2)

#exercise 3

list1 = []
list2 = []
list1 = input("Enter 1st list:").split()
list2 = input("enter 2nd list:").split()

merge_list = list1.copy()
for item in list2:
    if item not in merge_list:
        merge_list.append(item)

print(merge_list)

#exercise 4


list5 =[]
list5 = input("enter a list of num:").split()

min_num = min(list5)
max_num = max(list5)

print(min_num,max_num)

#exercise 5
city=("phnom penh","siem reap","battambang")
latitude=(11.5564,13.3622, 13.0957)
longtitude= (104.9282, 103.8597 , 103.2022)
coordinate = []
for i in range (len(city)):
    coordinate.append((city[i],latitude[i],longtitude[i]))
print(coordinate)

#exercise 6

dictionary = {}
num = int(input("Enter number of items: "))
for i in range(num):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    result = lambda x=value: x * 2
    dictionary[key] = result()

print("Dictionary:", dictionary)

#exercise 7

string = input("Enter a string: ")
result ={}

for i in range(len(string)):
    char = string[i]
    if char in result:
        result[char] = result[char] + 1
    else:
        result[char] = 1
print(result)
#exercise 8

dict1 = { "a": 1, "b": 2, "c": 3 }
dict2 = { "b": 3, "c": 4 }

merge_dict = dict1.copy()
for key, value in dict2.items():
    if key in merge_dict:
        merge_dict[key] += value
    else:
        merge_dict[key] = value
        
print(merge_dict)

#bonus exercise
