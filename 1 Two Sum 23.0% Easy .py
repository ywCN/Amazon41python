'''
Strategy: loop through the list by using enumerate to access both element and element index, and initialize a dictionary as a repository of data.
for each element in the list, the program will check if (target - current element) is in the dictionary. 
if it is in, return both indexes. If not, add the element as the key and its index as value in the dictionary.
'''

# comment to test commit and push
def twoSum(nums, target):
    d = {}

    for i, n in enumerate(nums):
        m = target - n

        if m in d:
            return [d[m], i]
        else:
            d[n] = i


print(twoSum([2, 7, 11, 15], 9))
