import random

#카드가 순서대로 있는 배열 = cards
#cards 리스트 생성
cards = []

#카드 개수 랜덤생성
cards_qty = 0
cards_qty = random.randint(2, 10)

#고른 숫자에 해당하는 개수만큼 cards 원소가 생길때까지 cards내 원소를 임의 생성하여 넣습니다
#스터디차원에서 중복없는 랜덤숫자를 만들어봅니다.(방법1)
for i in range(cards_qty):
    # 카드 숫자 임의 생성
    a = random.randint(1,cards_qty)
    #중복 안될 때까지 반복
    while a in cards:
        a = random.randint(1,cards_qty)
    #중복 안되는 숫자는 cards에 추가
    cards.append(a)

# 중복없는 랜덤숫자 리스트로 생성 (방법2)
# cards = random.sample(range(1,cards_qty),cards_qty)

# ------------------------------------------------------------------
# 여기까지 카드 생성 완료
# ------------------------------------------------------------------


# 카드 개수 확인. 현재는 의미없는 구문이나, 카드값을 외부에서 받는 함수로 제작 시, 필요한 구문임
cards_qty = len(cards)

print("card qty = ",cards_qty)
print("cards = ",cards)


#임시 그룹생성. 카드값과 카드 순서가 서로 이어지는 그룹을 말한다
temp_Grp = []

#카드 위치 기록용 리스트. 중복 검사 방지용
history_card_location = []

#게임 점수 채점용 숫자 리스트. 카드값과 카드 순서가 서로 이어지는 그룹의 카드 갯수가 각 원소의 값이 된다
score_num = []
score_num.append(int(0))                #최소 bias값 0


for i in range(cards_qty):
    #카드의 위치(몇번째 카드인지 표시). 1번째 카드로 시작한다. 카드 개수만큼 모두 시행해봐야 누락이 없다
    card_location = i
    # 카드 속 숫자. 1번째 카드 속 값으로 시작한다
    card_num = cards[card_location]
    #카드 위치가 이전에 확인한 위치라면 넘어간다
    if card_location in history_card_location:
        continue
    #카드 속 숫자가 임시 그룹에 없다면, 임시 그룹에 추가합니다
    #임시그룹에 추가한 뒤, 카드 속 숫자값이 다음 카드의 위치가 됩니다
    #카드 속 숫자가 임시 그룹에 있다면 반복문 종료
    while card_num not in temp_Grp:
        temp_Grp.append(card_num)
        card_location = card_num - 1
        history_card_location.append(card_location)             #카드 순서도 기록해둡니다
        card_num = cards[card_location]

    #임시 그룹 내 카드 개수를 저장 후 리셋
    score_num.append(len(temp_Grp))
    temp_Grp = []


#점수 채점용 숫자 리스트를 내림차순으로 정렬한다
print("score_number before sorted=",score_num)
score_num.sort(reverse=True)
print("score_number after sorted=",score_num)

#점수는 1,2번째 가장 큰값의 곱. 단, 최대값이 카드 갯수와 같으면 1차시도에서 끝난것이므로 점수는 0점.
if score_num[0] == cards_qty:
    answer = 0
else:
    answer = score_num[0] * score_num[1]

print("____________________________")
print("GAME MAX SCORE = ",answer)
print("____________________________")