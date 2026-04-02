# t = int(input())  # 테스트 케이스 개수 t를 입력받음

# for i in range(t):  # t 만큼 반복
#     a,b = map(int,input().split())
#     result = []
# print(a+b)



t = int(input())  # 테스트 케이스 개수

results = []  # 결과를 저장할 리스트를 반복문 '밖'에서 만듦

for i in range(t):
    a, b = map(int, input().split())
    results.append(a + b)  # 계산 결과를 리스트에 하나씩 추가

# 모든 입력이 끝난 뒤, 리스트에 담긴 내용을 하나씩 꺼내 출력
for res in results:
    print(res)