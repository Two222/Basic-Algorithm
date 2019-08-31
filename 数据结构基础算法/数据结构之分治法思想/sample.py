## 求解最大不连续子序列和
def max3(x,y,z):#求三个数的最大值
    max=x
    if y>max:
        max=y
    if z>max:
        max=z
        return max
    else:
        return max

def findmaxsum(alist): #求最大不连续子序列和
    length=len(alist)
    if len(alist)<=1: #递归结束条件
        return alist[0]
    mid=length//2
    left_list=alist[:mid]
    rigth_list=alist[mid:]
    leftmaxsum=findmaxsum(left_list) #递归解决左边序列最大不连续子序列和
    rightmaxsum=findmaxsum(rigth_list) #递归解决右边最大不连续子序列和
    max_left_right_sum=leftmaxsum+rightmaxsum #跨界情况，进行求和
    return max3(leftmaxsum,rightmaxsum,max_left_right_sum) #返回最大值

data = [1,2,3,4,-1,-5,6,-7]
a = findmaxsum(data)
print(a)


## 求解最大连续子序列和
def max3(x,y,z):#求三个数的最大值
    max=x
    if y>max:
        max=y
    if z>max:
        max=z
        return max
    else:
        return max

def findmaxsum_seq(alist): #求最大连续子序列和
    length=len(alist)
    if len(alist)==2: # 递归结束条件改变一下，改成两个的和即可
        return alist[0]+alist[1]
    mid=length//2
    left_list=alist[:mid]
    rigth_list=alist[mid:]
    leftmaxsum=findmaxsum(left_list) #递归解决左边序列最大连续子序列和
    rightmaxsum=findmaxsum(rigth_list) #递归解决右边最大连续子序列和
    max_left_right_sum=leftmaxsum+rightmaxsum #跨界情况，进行求和
    return max3(leftmaxsum,rightmaxsum,max_left_right_sum) #返回最大值

data = [1,-2,3,-4,11,-5,6,7]
b = findmaxsum_seq(data)
print(b)
