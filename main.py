# Python quiz Game

questions = ("How many element are in the periodic table?: ",
             "Whic animal lays the large eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Wich planet in the solar system is the hottets?: ")

options = (("A.  116", "B.  117", "C.  118", "D.  119"),
           ("A.  Wahle", "B.  Crocodrile", "C.  Elephant", "D.  Ostrich"),
           ("A.  Nitrogen", "B.  Oxigen", "C.  Carbon-Dioxide", "D.  Hydrogen"),
           ("A.  206", "B.  207", "C.  208", "D.  209"),
           ("A.  Mercury", "B.  Venus", "C.  Earth", "D.  Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0


question_num = 0


for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
