'''
문2-1) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def name_pro(emp):
    re1 = [sub('[0-9]{4}', '', i) for i in emp]
    re2 = [sub('[0-9]{3}$', '', i) for i in re1]
    print('names =',re2)

name_pro(emp)

# 함수 호출 
names = name_pro(emp)
print('names =', names)

def name_pro2(emp):
    from re import findall
    names = [findall('[가-힣]{3}', e)[0] for e in emp]
    return names

name_pro2(emp)






###teacher
from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def name_pro(emp):
    # 내용 채우기
    '''
    for + list
    names = [] # 빈 list
    for e in emp :
        tmp = findall('[가-힣]{3}', e)
        if tmp :
            names.append(tmp[0])
    '''
    # list 내포 : 변수 = [실행문  for 변수 in 열거형객체]
    names = [findall('[가-힣]{3}', e)[0] for e in emp]
    return names

# 함수 호출
names = name_pro(emp)
print('names =', names)
