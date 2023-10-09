import random
import time

def quiz_op(op):
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
    
    print(f"Press enter to end {op} and view results")
    print("Please input whole numbers only\n")
    
    while True:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        
        if operation == "addition":
            question = f"{num1} + {num2} = ?"
            answer = num1 + num2
        elif operation == "subtraction":
            # Ensure num1 is greater than num2 for subtraction
            num1, num2 = max(num1, num2), min(num1, num2)
            question = f"{num1} - {num2} = ?"
            answer = num1 - num2
        else:
            print("Invalid operation")
            break
        
        print(question)
        user_answer = input()
        
        if not user_answer:
            elapsed_time = time.time() - start_time
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            print(f"Correct answers: {correct_count}")
            print(f"Incorrect answers: {incorrect_count}")
            print(f"Time elapsed: {elapsed_time}")
            input(f"Press enter to end {operation}")
            break
        else:
            user_answer = int(user_answer)
            
            if user_answer == answer:
                print("✓\n")
                correct_count += 1
            else:
                print("✗\n")
                incorrect_count += 1

while True:
    print("Choose operation of choice:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Quit")
    
    choice = input()
    
    if choice == '1':
        quiz_operation("addition")
    elif choice == '2':
        quiz_operation("subtraction")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
