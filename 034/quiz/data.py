import requests
import json
import random
from question_model import Question

num = random.randint(10, 15)
params = {
    "amount": num,
    "type": "boolean"
}

def get_questions():
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = json.loads(response.text)["results"]
    results = []
    for item in data:
        q = item["question"]
        a = item["correct_answer"]
        newq = Question(q, a)
        results.append(newq)

    return results


question_data = get_questions()
