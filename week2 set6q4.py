quiz = {
    "What is the capital of France?": "Paris",
    "What is the currency of Japan?": "Yen",
    "What is the largest ocean in the world?": "Pacific Ocean",
    "What is the tallest mountain in the world?": "Mount Everest",
    "Who invented the light bulb?": "Thomas Edison",
    "Who wrote the novel 'Pride and Prejudice'?": "Jane Austen",
    "What is the name of the first man to walk on the moon?": "Neil Armstrong"
}

score = 0

for i in range(5):
    question = list(quiz.keys())[i]
    answer = input(question + ": ")
    if answer.lower() == quiz[question].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print("Your total score is:", score)