from quizGUI import QuizGUI
import requests

parameters = {"amount": 10, "category": 15, "difficulty": "medium", "type": "boolean"}
amount = 15
difficulty = "medium"
response = requests.get(url=f"https://opentdb.com/api.php?amount={amount}&category=18&difficulty={difficulty}&type=boolean")
response.raise_for_status()
question_data = response.json()['results']
print(question_data)
quizgui = QuizGUI(question_data)
