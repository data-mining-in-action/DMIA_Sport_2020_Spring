import requests

URL = 'https://script.google.com/macros/s/AKfycbzXHe24Mym-YIbYzXbAAzLx63yLAjEcYn91P-v9IyX4jdkWH8Q/exec'


def check(token, homework, task, answer):
    r = requests.post(url = URL , json={"token": token,
                                        "action": "hw",
                                        "hw": homework,
                                        "tsk": task,
                                        "answ": answer})
    return r.json()["response"]


def get_token(email):
    r = requests.post(url=URL, json={"action": "token",
                                     "email": email})
    return r.json()["response"]
