'''
step01 문제 

문) 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.

 << 출력 결과 >>
단계1 :  [10, 1, 5, 2, 10, 1, 5, 2]
단계2 : [10, 1, 5, 2, 10, 1, 5, 2, 20]
단계3 : [1, 2, 1, 2]
'''

lst = [10, 1, 5, 2] # list 생성
result=[]
# 단계1 : lst 원소를 2개 생성하여 result 변수에 저장/출력 
result = lst*2
print('단계1 : ', result) #[10, 1, 5, 2, 10, 1, 5, 2]

# 단계2 : lst의 첫번째 원소에 2를 곱하여 result 변수에 추가/출력
result.append(20)
print('단계2 :', result) #[10, 1, 5, 2, 10, 1, 5, 2, 20]

# 단계3 : result의 홀수 번째 원소만 result2 변수에 추가/출력
print(result[1::2])


#teacher
lst = [10, 1, 5, 2]  # list 생성

# 단계1 : lst 원소를 2개 생성하여 result 변수에 저장/출력
result = lst * 2
print('단계1 : ', result)  # [10, 1, 5, 2, 10, 1, 5, 2]

# 단계2 : lst의 첫번째 원소에 2를 곱하여 result 변수에 추가/출력
first = result[0] * 2
result.append(first)
print('단계2 :', result)  # [10, 1, 5, 2, 10, 1, 5, 2, 20]

# 단계3 : result의 홀수 번째 원소만 result2 변수에 추가/출력
result2 = result[1::2]
print(result2)  # [1, 2, 1, 2]

result2 = []  # 빈 list
i = 0
for n in result:
    if (i % 2) != 0:
        result2.append(n)
    i += 1

print('단계3 :', result2)

