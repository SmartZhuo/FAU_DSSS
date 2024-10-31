import random

def randomInt(min, max):
    """   
    Random to generate the integer between integer min and max
    input: min and max integer 
    output: random integer between min and max

    """
    return random.randint(min, max)


def randomCal():
    """ 
    
    Random to choice calculation from plus, minus, multiply
    input: None
    output: random operator from +, -, *

    """
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    """

    Do the calculation (depend "o" ) of n1 and n2 and return math question and its result
    input: number: n1, n2, operator: o
    output: math question and result

    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """

    Giving the random calculation(plus, minus, mutiply)
    Giving first random number between 1 and 10
    Giving second random number between 1 and 5
    verify your answer and give the score of your answer    
    """
    s = 0
    # total question number
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # giving total t_q random questions

    for _ in range(t_q):
        n1 = randomInt(1, 10); n2 = randomInt(1, 5); o = randomCal()

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. please give an integer.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
