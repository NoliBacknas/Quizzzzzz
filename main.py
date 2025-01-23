score = 0
 
question = "what is the capital of england?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "london":
    print("Correct!")
 
else:
    print("oops! the correct answer is london")
print(f"your score is: {score}")


question = "what is the capital of sweden?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "stockholm":
    print("Correct!")
 
else:
    print("oops! the correct answer is stockholm")
print(f"your score is: {score}")


question = "what is the capital of italy?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "rom":
    print("Correct!")
 
else:
    print("oops! the correct answer is rom")
print(f"your score is: {score}")

score = 0
 
question = "what is the capital of america?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "washington dc":
    print("Correct!")
 
else:
    print("oops! the correct answer is washington dc")
print(f"your score is: {score}")
