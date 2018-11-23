dic={}
dic['김'] = "김성식"
dic['윤'] = "윤정식"
dic['강'] = "강호동"

for s in dic.values():
    print(s)

for i in range(0,10,2): #Range 함수는 두번째 인자값(최종값) 보다 한단계 적은 숫자까지만 생성
    print(i)

for i in range(1,6):
    for j in range(i):
        print('*', end = "" ) #end=을 붙이면 줄바꿈 하지 않음
    print() #줄바꿈
        
