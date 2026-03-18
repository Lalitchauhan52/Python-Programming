questions = (("What is the chemical symbol for gold?"), 
             ("Which planet in our solar system is known as the RED PLANET?"), 
             ("Which cellular structure is commonly referred to as the POWERHOUSE of the cell?"),
             ("What is the hardest naturally occurring substance on Earth?"),
             ("Which fundamental force keeps the planets in orbit around the Sun?"))

options = (("A. Au", "B. Ag", "C. Fe", "D. Cu"),
           ("A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"),
           ("A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"),
           ("A. Diamond", "B. Graphite", "C. Corundum", "D. Topaz"),
           ("A. Gravity", "B. Electromagnetism", "C. Strong Nuclear Force", "D. Weak Nuclear Force"))

answers = ("A", "A", "B", "A", "A")
quesses = []
score = 0
questions_num = 0

for questiom in questions:
    print("-" * 40)
    print(questiom)
    for option in options[questions_num]:
        print(option)
    guess = input("enter your answer(A,B,C,D): ").upper()
    quesses.append(guess)
    if guess == answers[questions_num]:
        score += 1 
        print("CORRECT!")
    else:
        print(f"INCORRECT! The correct answer is {answers[questions_num]}")
    questions_num += 1
print(f"your score is {score}/{len(questions)}")

