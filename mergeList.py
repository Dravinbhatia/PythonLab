
list1 = ['A','App','a','d','ke','th','doc','awa']
list2 = ['y','tor','e','eps','ay',None,'le','n']
list3=[]
for i in list1:
    if len(list1)>len(list2):
        list3.append(i+list2[len(list2)-1-list1.index(i)])
    else:
        list3.append(list2[len(list2)-1-list1.index(i)]+i)
print(list3)
