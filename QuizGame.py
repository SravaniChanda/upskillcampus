import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('quiz_scores.db')
cursor = conn.cursor()

# Create a table to store scores if it doesn't exist already
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   score INTEGER)''')
conn.commit()

# Define questions
questions = [
    {
        'question': "Who developed Python Programming Language?",
        'options': ["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom"],
        'answer': "Guido van Rossum"
    },
    {
        'question': "Is Python case sensitive when dealing with identifiers?",
        'options': ["no", "yes", "machine dependent", "none of the mentioned"],
        'answer': "yes"
    },
    {
        'question': "Which of the following is the correct extension of the Python file?",
        'options': [".python",".pl",".py",".p"],
        'answer': ".py"
    },
    {
        'question': "Is Python code compiled or interpreted?",
        'options': ["Python code is both compiled and interpreted","Python code is neither compiled nor interpreted","Python code is only compiled"," Python code is only interpreted"],
        'answer': "Python code is both compiled and interpreted"
    },
    {
        'question': "Which keyword is used for function in Python language?",
        'options': ["Function","def","Fun","Define"],
        'answer': "def"
    },
    #add more questions here
]

# Function to ask a question
def ask_question(question):
    print(question['question'])
    for idx,option in enumerate(question['options'],start=1):
        print(f"{idx}.{option}")
    answer = input("Enter your answer: ").strip().lower()
    return answer == question['answer'].lower() or answer == str(question['options'].index(question['answer']) + 1)

# Function to start the quiz
def start_quiz(questions):
    username = input("Enter your username: ")
    score = 0
    random.shuffle(questions)
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Quiz ended! Your score: {score}/{len(questions)}")

    # Insert score into the database
    cursor.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
    conn.commit()
    print("Score saved to database.")

# Start the quiz
start_quiz(questions)

# Close the database connection
conn.close()
