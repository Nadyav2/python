# function which return reverse of a string

def Palindrome(k):
    return k == k[::-1]

k = "Chronicles"
ans = Palindrome(k)

if ans:
    print("Yes")
else:
    print("No")
