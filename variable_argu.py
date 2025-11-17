# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name : {0}\tAge : {1}\t".format(name, age), end=" ") # print without newline
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *langs): # *langs : variable-length arguments
    print("Name : {0}\tAge : {1}\t".format(name, age), end=" ")
    for lang in langs:
        print(lang, end=" ")
    print()

profile("Jae", 25, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("Steve", 30, "Kotlin", "Swift")