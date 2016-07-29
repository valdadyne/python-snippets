import input

def tribonacci():

    a=0
    x=input.user()
    ans=[0,0,1]


    while a<x:
        a=int(ans[len(ans) - 3])+int(ans[len(ans) - 2])+int(ans[len(ans) - 1])
        ans.append(a)
    return ans

print tribonacci()