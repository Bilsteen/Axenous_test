#Question 3:
#Retrieve the positions of numbers which are divisible by 2 
#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] , 
#the output should be neat and understandable, no restrictions are kept on the format of representation of the #output.  


def even_positions(nums):
    position = []
    counter = 1
    for num in nums:
        if num%2 == 0:
            position.append(counter)
        counter += 1
    return position

output = even_positions([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(f"The position of even numbers in the list are {output}")