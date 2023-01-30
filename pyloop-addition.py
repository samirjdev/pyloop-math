import random
import time

start_time = time.time()

correct_count = 0
incorrect_count = 0
print("Press enter to end and view results")
print("Please input whole numbers only\n")


while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    answer = num1 + num2
        
    print(f"{num1} + {num2} = ?")
    user_answer = input()

    if not user_answer:
        elapsed_time = time.time() - start_time
            
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            
        print(f"Correct answers: {correct_count}")
        print(f"Incorrect answers: {incorrect_count}")
        print(f"Time elapsed: {elapsed_time}")
        input("Press enter to exit")
            
        break
        
    else:
        user_answer = int(user_answer)
            
        if user_answer == answer:
            print("✓\n")
            correct_count += 1
                
        else:
            print("✗\n")
            incorrect_count += 1
