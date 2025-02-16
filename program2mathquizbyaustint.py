import random

def generate_question():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def check_answer(num1, num2, user_answer):
    correct_answer = num1 + num2
    return user_answer == correct_answer, correct_answer

def main():
    num1, num2 = generate_question()
    print(f"  {num1}\n+ {num2}\n-----")
    user_answer = int(input("Enter your answer: "))
    
    is_correct, correct_answer = check_answer(num1, num2, user_answer)
    
    if is_correct:
        print("Congratulations, nerd! Your answer is correct.")
    else:
        print(f"Sorry little guy, the correct answer is {correct_answer}.")

if __name__ == "__main__":
    main()
