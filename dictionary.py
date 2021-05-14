pairs = {'태연':'what do i call you', 'pH-1':'365&7','미란이':'Dasiy'}
print(pairs)

#추가 : 딕셔너리 변수[키] = value
pairs['선미'] = '꼬리'
print(pairs)

#삭제 : del 변수[키]
del pairs['태연'] 
print(pairs)

#key value 값 찾기 : 딕셔너리 변수.get(키)
print(pairs.get('미란이'))
