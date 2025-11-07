##filter(function, iterable)
#-----------------------------------------------------------------------
#find out how to do filter lambda ******
from functools import reduce

    #nums = [1,2,3,4,5,6,7,8,9,10]

    #filtered_list_lambda = list(filter(lambda x: x % 2 == 0, nums))
    #print(filtered_list_lambda)

# Calculate and display the sum
    #total = sum(nums)
    #print("Sum of numbers:", total)

#given a list from num 1-10
#calculate and display the sum of numbers of the list

#-----------------------------------------------------------------------
#find out how to use reduce ******
    #nums2 = [1,2,3,4,5,6,7,8,9,10]
    #reduced_list = list(reduce(lambda x: x % 2 == 0, nums2))
    #print(reduced_list)
#need to print out the sum
#-----------------------------------------------------------------------

#zip
#define 2 list, the first containing names, 3 or 4 names
#and the second list containing the age
names = ["Brandon", "James", "Oscar", "Smith"]
ages = [28, 24, 23, 31]
#combine names and ages into tupple
#use zip function
combined_data = zip(names, ages)
print(list(combined_data))

#-----------------------------------------------------------------------
#unzip
zipped_data = [('Alice', 30), ('Bob', 25)]
unzipped_names, unzipped_ages = zip(*zipped_data)

print(unzipped_names)
print(unzipped_ages)