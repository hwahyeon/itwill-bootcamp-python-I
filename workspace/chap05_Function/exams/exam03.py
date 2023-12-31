'''
 문3) 다음은 중첩함수를 이용하여 은행계좌 함수를 정의한 것이다. 

<조건1> outer 함수 : bank_account() -> balance(잔액) 초기화, Inner함수 포함
<조건2> inner 함수 : getBalance() -> 잔액보기 : balance 출력
                    deposit() -> 입금하기 : balance += money
                    withdraw() -> 출금하기 : balance -= money
<조건4> 예외처리 : 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.’ 메시지 출력
<조건3> 기타 나머지는 출력 예시 참조

    입금하기와 출금하기 함수 내용을 채우시오.
    <조건1> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력 
    <조건2> 기타 나머지는 출력 예시 참조

<<화면 출력 예시1>>
최초 계좌의 잔액을 입력하세요 : 1000
현재 계좌 잔액은 1000원 입니다.
입금액을 입력하세요 : 10000
10000원 입금 후 잔액은 11000원 입니다.
출금액을 입력하세요 : 8000
8000원 출금 후 잔액은 3000원 입니다.

<<화면 출력 예시2>>
최초 계좌의 잔액을 입력하세요 : 1000
현재 계좌 잔액은 1000원 입니다.
입금액을 입력하세요 : 20000
20000원 입금 후 잔액은 21000원 입니다.
출금액을 입력하세요 : 30000
잔액이 부족합니다.
30000원 출금 후 잔액은 21000원 입니다.

'''

def bank_account(bal):
    balance = bal  # 잔액(balance) : outer변수

    def getBalance():  # 잔액확인(getter)
        return balance

    def deposit(money):  # 입금하기(setter)
        if money < 0:
            print("금액을 확인하세요.")
        else:
            nonlocal balance
            balance += money

    def withdraw(money):  # 출금하기(setter)
        nonlocal balance
        if balance < money:
            print("잔액이 부족합니다.")
        else:
            balance -= money

    return getBalance, deposit, withdraw  # 클로저 함수 리턴

# 잔액 입력
bal = int(input('최초 계좌의 잔액을 입력하세요 : '))

# 함수 호출
getBalance, deposit, withdraw = bank_account(bal) # outer 호출

# 잔액 확인
print('현재 계좌 잔액은 {}원 입니다.'.format(getBalance()))

# 계좌에 입금
money = int(input('입금액을 입력하세요 : '))
deposit(money)
print('{}원 입금후 잔액은 {}원 입니다.'.format(money, getBalance()))

# 계좌에 출금
money = int(input('출금액을 입력하세요 : '))
withdraw(money)
print('{}원 입금후 잔액은 {}원 입니다.'.format(money, getBalance()))









