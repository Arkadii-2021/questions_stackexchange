from pprint import pprint
import requests

def get_questions():
    url = "https://api.stackexchange.com/2.3/questions"
    params = {"fromdate": 1630454400, "todate": 1632096000, "order": "desc", "sort": "activity", "tagged": "Python", "site": "stackoverflow"}
    response = requests.get(url, headers={'User-agent': 'netology'}, params=params)
    questions = response.json()
    questions_list = []
    title_list = []
    for quest in questions['items']:
        questions_list.append(quest)
    for title in questions_list:
        title_list.append(title['title'])
    return title_list
pprint(get_questions())