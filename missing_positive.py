
def first_missing_positive(numbers):
    #ignore all non-positive numbers 
    numbers=[num for num in numbers if num>0]
    #set to numbers
    num_set=set(numbers)


    #start checking from 1 since it is smallest positive integer
    missing_positive=1
    while True:
        if missing_positive not in num_set:
            return missing_positive
        missing_positive += 1
    

print(first_missing_positive([3, 4, -1, 1])) 
print(first_missing_positive([1, 2, 0]))      
print(first_missing_positive([7, 8, 9, 11, 12]))  

