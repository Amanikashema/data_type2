my_list=[56,78,34,21,56,34,125,45,89,75,12,56]
my_list.sort()
print(my_list)

total=sum(my_list) #using a function of sum to add the total
print("The sum of all of the element is:", total)

print("The smallest number in the list is:", min(my_list))

print("The largest number in the list is:",max(my_list))

my_list=list(set(my_list))
print("List after removing duplicate elements", my_list)





