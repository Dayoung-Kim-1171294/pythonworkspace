print('python', 'java', sep=', ', end='? ')
print('무엇이 더 재밌을까요?')

import sys
print('python', 'java', file=sys.stdout) # 표준 출력
print('python', 'java', file=sys.stderr) # 표준 에러

scores = {'수학':0, '영어':50, '코딩':100}
# items() : key와 value를 튜플 형태로 반환
for subject, score in scores.items():
    print(subject.ljust(2), str(score).rjust(4), sep=': ')

for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")