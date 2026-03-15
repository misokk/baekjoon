n, m = map(int, input().split()) #n,m을 입력받아 int로 변환
cards = list(map(int, input().split())) #카드에 쓰여 있는 수 들을 list화 하여 저장
result = 0 #문제 조건에 적합한 수를 저장하여 반환하기 위한 변수 result 선언
for i in range(n): #4~10 3개의 카드를 뽑아야 하며 이에 대한 모든 경우의 수를 살펴보기 위해 3중 for문을 이용한다 첫 for 문에서는 0 두번쨰 1 세번째 2~N 값을 다 더해 세 값이 M보다 클 경우 continue 아니면 result에 저장 이렇게 반복하다 M에는 가장 M에 가까운 수 저장
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                result = max(result, cards[i]+ cards[j] + cards[k])
print(result)