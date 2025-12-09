# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# a: append
# score_file = open("score.txt", "a", encoding="utf8")
# print("과학 : 80", file=score_file) 
# score_file.write("코딩 : 100")
# score_file.write("\nAI : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장, readlines()로 가져오면 한줄씩 끊어서 가져오고 커서는 해당 줄의 다음줄로 이동
# for line in lines:
#     print(line, end="") # 줄바꿈이 이미 포함되어 있어서 end=""

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")

lines = score_file.readlines()
for line in lines:
    print(line, end="")


# while line:
#     print(line, end="")
#     line = score_file.readline()

score_file.close()


