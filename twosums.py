def twosums(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target-nums[i]==nums[j]:
                return[i,j]
    return None
test=list(map(int,input("enter the list element:").split()))
target=int(input("enter the target value:"))
print(twosums(test,target))                
