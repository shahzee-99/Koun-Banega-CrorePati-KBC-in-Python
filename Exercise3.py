query = [
    "What is the largest ocean on Earth?", 
    "Who was the first person to step on the Moon?",
    "What is the capital of France?",
    "What is the smallest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the hardest natural substance on Earth?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for gold?",
    "In which year did the Titanic sink?",
    "What is the largest mammal?",
    "Who developed the theory of relativity?",
    "What is the tallest mountain in the world?",
]

options = [
    "a) Atlantic Ocean b) Indian Ocean c) Arctic Ocean d) Pacific Ocean",
    "a) Yuri Gagarin b) Neil Armstrong c) Buzz Aldrin d) Michael Collins",
    "a) Paris b) Berlin c) Madrid d) Rome",
    "a) Earth b) Mars c) Mercury d) Venus",
    "a) Charles Dickens b) Jane Austen c) William Shakespeare d) Mark Twain",
    "a) Gold b) Iron c) Diamond d) Platinum",
    "a) Vincent van Gogh b) Pablo Picasso c) Leonardo da Vinci d) Michelangelo",
    "a) Ag b) Au c) Pb d) Fe",
    "a) 1905 b) 1912 c) 1918 d) 1923",
    "a) Elephant b) Blue Whale c) Great White Shark d) Giraffe",
    "a) Isaac Newton b) Nikola Tesla c) Albert Einstein d) Galileo Galilei",
    "a) K2 b) Kangchenjunga c) Lhotse d) Mount Everest",
]

Correct_ans = [
    "d) Pacific Ocean", 
    "b) Neil Armstrong",  
    "a) Paris",
    "c) Mercury",
    "c) William Shakespeare",
    "c) Diamond",
    "c) Leonardo da Vinci",
    "b) Au",
    "b) 1912",
    "b) Blue Whale",
    "c) Albert Einstein",
    "d) Mount Everest",
]

Rewards = [
    100,
    200,
    300,
    500,
    1000,
    2000,
    4000,
    8000,
    16000,
    32000,
    64000,
    125000,
]

total_amount = 0
wrong_answers = 0

for i in range(len(query)):
    print(query[i])
    print(options[i])
    print(f"Reward: ${Rewards[i]}")
    print()

    print('Write Your Answer Like This "Example a) Allah".')
    ans = input("Write Your Answer: ").strip().lower()
    print()

    correct = False
    for j in range(len(Correct_ans)):
        if ans == Correct_ans[j].lower():
            correct = True
            break

    if correct:
        print("Your Answer Is Correct!")
        total_amount += Rewards[i]
    else:
        print("Your Answer Is Wrong!")
        wrong_answers += 1

    if wrong_answers == 3:
        print("You have reached 3 wrong answers. Game over!")
        break

print(f"\nTotal Amount Won: ${total_amount}")
