#조합
# visited=[3]*5
# A=[0]*3
#
# data=['a','b','c','d','e']
# def go(now_index):
#     if now_index==3:
#         result=[]
#         for i in range(0,3):
#             result.append(data[A[i]])
#         print(result)
#         return
#     for i in range(0,5):
#         if visited[i]>0:
#             if now_index>0:
#                 if A[now_index-1]>=i:
#                     continue
#             visited[i] = visited[i]-1
#             A[now_index]=i
#             go(now_index+1)
#             visited[i] = visited[i]+1
# go(0)



#   
# 중복조합
# def combi(index, combination, length):
#     global count
#     if len(combination) == length:
#         print(combination)
#         count+=1
#         return
#     if index>=len(data):
#         return
#     combi(index,combination+[data[index]],length)
#     combi(index+1,combination,length)


count = 0
data = [1,2,3,4,5]
combi(0,[],3)
print(count)

