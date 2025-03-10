




nums = [1,2,3,4]

def checking(nums):
    repeat = False
    for element in nums:
        count = 0
        check = element
        for value in nums:
            if value == check:
                count += 1
                if count > 1:
                    repeat = True
            else:
                repeat = False
    return repeat

# print(checking(nums))

def product_array(nums):
    x = len(nums)
    answer = []
    for i in range(x):
        product = 1
        for j in range(x):
            if i != j:
                product *= nums[j]
        answer.insert(i, product)
    print(answer)

# product_array(nums)
s = "abcsad"
t = "bcadsx"
def is_anagram(s, t):
    if len(s) == len(t):
        for i in s:
            if s.count(i) == t.count(i):
                a = "is anagram"
            else:
                a = "is not anagram"
    else:
        a = "is not anagram"
    return a

print(is_anagram(s,t))
