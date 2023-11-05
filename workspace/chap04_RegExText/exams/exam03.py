'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    
   <출력 예시> 
유관순 750905-******* 
홍길동 850905-******* 
강감찬 770210-*******  
'''

import re # 정규표현식 패키지 임포트

person = """유관순 750905-2049118
홍길동 850905-1059119
강호동 790101-5142142
강감찬 770210-1542001"""

person_lst = person.split('\n')
person_lst
from re import match, findall


for i in person_lst:
    result = match("[가-힣]{3} \\d{6}-[1-4]\\d{6}", i)
    if result: #패턴과 일치된 주민번호
        jumin = result[0]
        print(jumin)

        jumin2 = jumin[:10]+"-*******"
        print(jumin2)

# teacher
for p in person.split('\n') :
    #re.findall()
    result = re.match('[가-힣]{3} \\d{6}-[1-4]\\d{6}', p)
    if result :  #패턴과 일치된 주민번호
        jumin = result[0]
        print(jumin)
        jumin2 = jumin[:10]+"-*******"
        print(jumin2)





