nums = [1,2,3,4,5,6,7,8,9,10]

#Squaring each num in nums into new list
my_list = [n *n for n in nums]
print(my_list)

#giving only even numbers of nums
my_list2 = [n for n in nums if n%2 == 0]
print(my_list2)

#Grouping abcd to each n in nums; nested for loop
my_list3 = [(letter,num) for num in range(4) for letter in 'abcd']
print(my_list3)


#Dictionay comprehension
names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

my_dict = {name: hero for name, hero in zip (names,heros)}
print(my_dict)

#Set comprehension
nums = [1,1,2,1,3,4,4,5,5,6,7,9,10,9,8]
my_set = set()
my_set = {n for n in nums}
print(my_set)


