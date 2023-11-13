
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

def solution(record):
    answer = []
    raw_data = []                   #record를 변환한 2차원 리스트
    ids_nick = {}               #아이디 별 최신닉네임 딕셔너리

    #2차원 리스트 형태로 데이터 변환
    for i in range(len(record)):
        raw_element = record[i].split(" ")
        raw_data.append(raw_element)
        print(raw_data)

    #아이디 별 최신 닉네임 딕셔너리 입력
    for i in range(len(raw_data)):
        temp_status = str(raw_data[i][0])
        temp_id = str(raw_data[i][1])
        #아이디별 닉네임을 갱신한다. 단, Leave인 경우, 닉네임이 없으므로 생략함
        if temp_status == "Leave":
            continue
        else:
            temp_nick = str(raw_data[i][2])
            ids_nick[temp_id] = temp_nick
    print(ids_nick)

    #리턴 값 생성
    for i in range(len(raw_data)):
        temp_status = str(raw_data[i][0])
        temp_id = str(raw_data[i][1])
        else:
            #상태별 문장 생성
            #아이디를 통해 딕셔너리 속 최신닉네임 값 호출
            if temp_status == "Enter":
                temp_answer = str(ids_nick[temp_id])+"님이 들어왔습니다."
            elif temp_status == "Leave":
                temp_answer = str(ids_nick[temp_id])+"님이 나갔습니다."
            else:
                continue
            answer.append(temp_answer)

    return answer

a = solution(record)
print("answer = ", a)
