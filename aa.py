# list=[]
# number1=input("请输入第1个数：")
# if type(number1)!=int:
#     print("您的输入错误，只能输入数字，请重新输入！")
#     number1 = input("请输入第1个数：")
# number2=input("请输入第2个数：")
# number3=input("请输入第3个数：")
# number4=input("请输入第4个数：")
# number5=input("请输入第5个数：")
# list.append(number1)
# list.append(number2)
# list.append(number3)
# list.append(number4)
# list.append(number5)
# print("您一共输入了5个数字:",list)
# list.sort()
# print("排序后的结果是：",list)


# list=[1,3,3,5,6,8,8,9]
# # print(list)
# for yuansu in list:
#     if list.count(yuansu)>1:
#         list.remove(yuansu)
#     print(list)


# def findMax(x,y,z):
#     if x>y:
#         if x>z:
#             print(x)
#         else:
#             print(z)
#     elif x<y:
#         if y>z:
#             print(y)
#         else:
#             print(z)
#
# if __name__ == '__main__':
#     max=findMax(4,8,2)
#     max = findMax(1, 3, 2)


# list=[3,4,51,2,8]
# list.sort(reverse=True)
# print(list[0])
# # len(list)-1
# def zhanzhuan(a,b):
#     if a>b:
#         if a%b==0:
#             print("a,b的最大公约数是：%s"%(a,b),b)
#         else:
#             while True:
#                 r = a % b
#                 a = b
#                 b = r
#                 if r==0:
#                     print(b)
#                     break
#                 else:
#                     continue
# zhanzhuan(64,24)
# a,b=input("请输入两个整数，用逗号分隔：").split(",")
# a,b=int(a),int(b)
# c=a%b
# while c:
#     a,b=b,c
#     c=a%b
# print(b)


# def shu(a,b):
#     min=a if a<b else b
#     for i in range(1,min+1):
#         if a%i==0 and b%i==0:
#             gongyuesu=i
#     print(gongyuesu)
#
# shu(24,12)
# shu(2,4)
# shu(3,6)
# shu(4,6)

# def jiecheng(m):
#     if m==1:
#         print("1")
#     else:
#         chengji =1
#         for i in range(1,m+1):
#             chengji=chengji*i           #1,2,3
#         print(chengji)
# input_number=input("请输入一个正整数：")
# number=int(input_number)
# jiecheng(number)



# def target(list,target):
#     list.sort()
#     start=0
#     end=len(list)
#     count=0
#     while start<end:
#         count = count + 1
#         mid = (start + end) // 2
#         print("list:",list)
#         print("mid:%s,list[mid]:%s"%(mid,list[mid]))
#         if target==list[mid]:
#             print("次数：%s"%(count),target)
#             break
#             # return "次数：%s"%(count),target
#         elif target>list[mid]:
#             start=mid+1
#         elif target<list[mid]:
#             end=mid-1
# target([1,2,0,3,4,5,6,7,9],4)





# def tarList(list,target):
#     count = 0
#     for i in range(0,len(list)):
#         if target==list[i]:
#             print("次数：%s"%(count),target)
#         else:
#             count=count+1
# tarList([2,0,1,5,4,3,6,7,89],3)


# str="abcaabbccabcdefabc"
# def changchuan(str):
#     maxLen=1
#     list=[str[0]]
#     for i in range(0,len(str)):
#         while str[i] in list:
#             list.pop(0)
#         list.append(str[i])
#         if len(list)>maxLen:
#             maxLen=len(list)
#     return list,maxLen
# print(changchuan(str))


# import random
# print(random.randint(0,100))
# str="abcd"
# print(str[::-1])

# str1="abcddcba"
# str2="abcffcba"
# str3="abc"
# def huiwen(str):
#     if str==str[::-1]:
#         print("True")
#     else:
#         print("False")
# huiwen(str1)
# huiwen(str2)
# huiwen(str3)

# import random
# list=[]
# for i in range(0,101):
#     i =random.randint(0,100)
#     list.append(i)
# file=open("1.txt",'a')
# file.write(str(list))
# # for line in file.readlines():
# #     print(line)
# file.close()



# # print(set(list))
# def maopao(list):
# #     n = len(arr)
# #
# #     # 遍历所有数组元素
# #     for i in range(n):
# #
# #         # Last i elements are already in place
# #         for j in range(0, n - i - 1):
# #
# #             if arr[j] > arr[j + 1]:
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #
# #
# # arr = [64, 34, 25, 12, 22, 11, 90]
# #
# # maopao(arr)
# # print(arr)
#     for i in range(0,len(list)):
#         for j in range(0,len(list)-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#   # print(str(list))
# # list=[3, 4, 0, 5, 2, 1, 6]
# # maopao(list)
# print(maopao([3, 4, 0, 5, 2, 1, 6]))



# list=[1,0,2,0,3]
# dict={"a":24,"g":52,"i":12}
# print(dict.items())
# print(sorted(dict.items(),key=lambda x:x[1]))

# list=[{"name":"xiaohua","age":24},{"name":"b","age":30},{"name":"c","age":25}]
# print(sorted(list,key=lambda x:x['age'],reverse=False))


# print([x*11 for x in range(1,10)])
list=['b','d','c','b','c','a','a']
l2=set(list)
print(l2)
























