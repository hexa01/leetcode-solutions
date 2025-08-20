def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def numSum(n):
    if n == 0:
        return 0
    a = n % 10
    n = n // 10
    return a + numSum(n)

def binaryString(s, n):
    if len(s) == n:
        return [s]
    return binaryString(s+'0',n) + binaryString(s+'1',n)

def toh(n,s,d,h):
    if n == 1:
        print("Disk " , n , " moving from " , s ,  "--->" , d)
        return
    toh(n-1,s,h,d)
    print("Disk " , n , " moving from " , s , "--->" , d)
    toh(n-1,h,d,s)

def subsets(nums):
    result = []
    
    def helper(i,current):
        if i == len(nums):
            result.append(current)
            return
        pick = current + [nums[i]]
        not_pick = current
        helper(i+1,not_pick)
        helper(i+1,pick)

    helper(0,[])
    return result


# print(factorial(0))
# print(fib(7))
# print(numSum(12345))
# print(binaryString("", 3))
# toh(3,"S","D","H")
print(subsets([1,2,3]))