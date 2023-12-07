from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

urls = ["https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19-travel-advice-for-the-general-public",
'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19-risks-and-safety-for-older-people']

data = dict()

for url in urls:
    req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})

    page = urlopen(req)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    qa_details_title = soup.find("h1", class_="qa-details__title").getText()
    
    qa_details_content = soup.find_all("div", itemtype = "https://schema.org/Question")
    for question_answer_tagObj in qa_details_content:
        question_answer_raw = question_answer_tagObj.getText()
        question_answer_clean = re.sub("([ \t]*\n){3,}", "\n", question_answer_raw).split('\n')[1:-1]

        data.setdefault(qa_details_title, []).append({'question': question_answer_clean[0], 'answer' : question_answer_clean[1]})

with open("who_qa_dataset.json", "w") as write_file:
    json.dump(data, write_file)