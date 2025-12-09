def std_weight(height, gender):
    # 딕셔너리(dictionary) 리터럴
    standard_weights = {
        'male': (height - 100) * 0.9,
        'female': (height - 100) * 0.85
    }
    print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, standard_weights[gender]))

std_weight(180, 'female')
std_weight(182, 'male')

