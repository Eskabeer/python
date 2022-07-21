# string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
# print(string.split())

# new_list = [n for n in string.split() if 'y' in n or 'Y' in n]

# print(new_list)

sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

result = [letter for letter in sentence if letter not in 'a,e,i,o,u, " "']
print(result)
