li = [3,1,"배가",4,"고파요",5,1]

print(li[2])
print(li[2:5])

#1. 리스트 길이를 구해주는 내장함수 : len()
print(len(li))

#2. 리스트를 오름차순으로 정렬 : sort()
li2 = [3,1,4,5,2]
#li2.sort() 
#print(li2) 

#sorted()
print(sorted(li2))
print(li2)

#2-퀴즈. 리스트를 내림차순 정렬 : sort(reverse=True)
li2.sort(reverse=True)
print(li2)

#3. 리스트 내의 특정 원소 인덱스를 반환하는 함수 : 리스트변수.index()
print(li.index("배가"))

#4. 리스트 내의 특정 원소의 갯수를 세어주는 함수 : 리스트변수.count()
print(li.count(1))
