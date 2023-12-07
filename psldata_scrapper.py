
"""
    PSLData_scrapper.ipynb
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

# !chromedriver --version

# !systemctl restart snapd

# !snap install chromium

# !pip install selenium

import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.addArguments("disable-infobars")
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()

# Web scrapper for infinite scrolling page

urls = [
# Match 1 Lahore Innings
"https://www.espn.in/cricket/series/8679/commentary/1354924/multan-sultans-vs-lahore-qalandars-1st-match-pakistan-super-league-2022-23?innings=1",
# Match 2 KK Innings
"https://www.espn.in/cricket/series/8679/commentary/1354925/karachi-kings-vs-peshawar-zalmi-2nd-match-pakistan-super-league-2022-23",
# Match 2 PZ Innings 
"https://www.espn.in/cricket/series/8679/commentary/1354925/karachi-kings-vs-peshawar-zalmi-2nd-match-pakistan-super-league-2022-23?innings=1",
# Match 3 QG Innings
"https://www.espn.in/cricket/series/8679/commentary/1354926/multan-sultans-vs-quetta-gladiators-3rd-match-pakistan-super-league-2022-23?innings=1",
# Match 4 isl
"https://www.espn.in/cricket/series/8679/commentary/1354927/karachi-kings-vs-islamabad-united-4th-match-pakistan-super-league-2022-23",
# Match 4 KK
"https://www.espn.in/cricket/series/8679/commentary/1354927/karachi-kings-vs-islamabad-united-4th-match-pakistan-super-league-2022-23?innings=1",

# Match 5 PZ
"https://www.espn.in/cricket/series/8679/commentary/1354928/multan-sultans-vs-peshawar-zalmi-5th-match-pakistan-super-league-2022-23",
# Match 5
"https://www.espn.in/cricket/series/8679/commentary/1354928/multan-sultans-vs-peshawar-zalmi-5th-match-pakistan-super-league-2022-23?innings=1",
# Match 6 QG
"https://www.espn.in/cricket/series/8679/commentary/1354929/karachi-kings-vs-quetta-gladiators-6th-match-pakistan-super-league-2022-23?innings=1",
# Match 7
"https://www.espn.in/cricket/series/8679/commentary/1354930/multan-sultans-vs-islamabad-united-7th-match-pakistan-super-league-2022-23?innings=1",
# Match 8
"https://www.espn.in/cricket/series/8679/commentary/1354931/karachi-kings-vs-lahore-qalandars-8th-match-pakistan-super-league-2022-23?innings=1"
# Match 9 
"https://www.espn.in/cricket/series/8679/commentary/1354932/quetta-gladiators-vs-peshawar-zalmi-9th-match-pakistan-super-league-2022-23?innings=1",
# Match 10
"https://www.espn.in/cricket/series/8679/commentary/1354933/quetta-gladiators-vs-lahore-qalandars-10th-match-pakistan-super-league-2022-23?innings=1"
# Match 11 MS
"https://www.espn.in/cricket/series/8679/commentary/1354934/multan-sultans-vs-karachi-kings-11th-match-pakistan-super-league-2022-23",
# Match 12 PZ
"https://www.espn.in/cricket/series/8679/commentary/1354935/peshawar-zalmi-vs-islamabad-united-12th-match-pakistan-super-league-2022-23?innings=1",
# Match 13
"https://www.espn.in/cricket/series/8679/commentary/1354936/quetta-gladiators-vs-islamabad-united-13th-match-pakistan-super-league-2022-23?innings=1",
# Match 14 KK
"https://www.espn.in/cricket/series/8679/commentary/1354937/karachi-kings-vs-multan-sultans-14th-match-pakistan-super-league-2022-23?innings=1",
# Match 15
"https://www.espn.in/cricket/series/8679/commentary/1354938/lahore-qalandars-vs-peshawar-zalmi-15th-match-pakistan-super-league-2022-23?innings=1",
# Match 16
"https://www.espn.in/cricket/series/8679/commentary/1354939/lahore-qalandars-vs-islamabad-united-16th-match-pakistan-super-league-2022-23?innings=1",
# Match 17
"https://www.espn.in/cricket/series/8679/commentary/1354940/peshawar-zalmi-vs-karachi-kings-17th-match-pakistan-super-league-2022-23?innings=1",
# Match 18
"https://www.espn.in/cricket/series/8679/commentary/1354941/lahore-qalandars-vs-quetta-gladiators-18th-match-pakistan-super-league-2022-23?innings=1",
# Match 19
"https://www.espn.in/cricket/series/8679/commentary/1354942/islamabad-united-vs-karachi-kings-19th-match-pakistan-super-league-2022-23?innings=1",
# Match 20
"https://www.espn.in/cricket/series/8679/commentary/1354943/lahore-qalandars-vs-multan-sultans-20th-match-pakistan-super-league-2022-23?innings=1",
# Match 21
"https://www.espn.in/cricket/series/8679/commentary/1354944/islamabad-united-vs-quetta-gladiators-21st-match-pakistan-super-league-2022-23?innings=1",
# Match 22
"https://www.espn.in/cricket/series/8679/commentary/1354945/quetta-gladiators-vs-karachi-kings-22nd-match-pakistan-super-league-2022-23?innings=1",
# Match 23
"https://www.espn.in/cricket/series/8679/commentary/1354946/peshawar-zalmi-vs-lahore-qalandars-23rd-match-pakistan-super-league-2022-23?innings=1",
# Match 24
"https://www.espn.in/cricket/series/8679/commentary/1354947/islamabad-united-vs-multan-sultans-24th-match-pakistan-super-league-2022-23?innings=1",
# Match 25
"https://www.espn.in/cricket/series/8679/commentary/1354948/peshawar-zalmi-vs-quetta-gladiators-25th-match-pakistan-super-league-2022-23?innings=1",
# Match 26
"https://www.espn.in/cricket/series/8679/commentary/1354949/islamabad-united-vs-lahore-qalandars-26th-match-pakistan-super-league-2022-23?innings=1",
# Match 27
"https://www.espn.in/cricket/series/8679/commentary/1354950/peshawar-zalmi-vs-multan-sultans-27th-match-pakistan-super-league-2022-23?innings=1",
# Match 28
"https://www.espn.in/cricket/series/8679/commentary/1354951/quetta-gladiators-vs-multan-sultans-28th-match-pakistan-super-league-2022-23?innings=1",
# Match 29
"https://www.espn.in/cricket/series/8679/commentary/1354952/islamabad-united-vs-peshawar-zalmi-29th-match-pakistan-super-league-2022-23?innings=1",
# Match 30
"https://www.espn.in/cricket/series/8679/commentary/1354953/lahore-qalandars-vs-karachi-kings-30th-match-pakistan-super-league-2022-23?innings=1",
# Match 31
"https://www.espn.in/cricket/series/8679/commentary/1354954/lahore-qalandars-vs-multan-sultans-qualifier-pakistan-super-league-2022-23?innings=1",
# Match 32
"https://www.espn.in/cricket/series/8679/commentary/1354955/islamabad-united-vs-peshawar-zalmi-eliminator-1-pakistan-super-league-2022-23?innings=1",
# Match 33
"https://www.espn.in/cricket/series/8679/commentary/1354956/lahore-qalandars-vs-peshawar-zalmi-eliminator-2-pakistan-super-league-2022-23?innings=1",
# Match 34
"https://www.espn.in/cricket/series/8679/commentary/1354957/lahore-qalandars-vs-multan-sultans-final-pakistan-super-league-2022-23?innings=1",
# Match 9 Quetta
"https://www.espn.in/cricket/series/8679/commentary/1354932/quetta-gladiators-vs-peshawar-zalmi-9th-match-pakistan-super-league-2022-23?innings=1",
# Match 10 peshawar

"https://www.espn.in/cricket/series/8679/commentary/1354932/quetta-gladiators-vs-peshawar-zalmi-9th-match-pakistan-super-league-2022-23?innings=2",

# Match 26 Islamabad
"https://www.espn.in/cricket/series/8679/commentary/1354949/islamabad-united-vs-lahore-qalandars-26th-match-pakistan-super-league-2022-23",
# Match 30 Karachi
"https://www.espn.in/cricket/series/8679/commentary/1354953/lahore-qalandars-vs-karachi-kings-30th-match-pakistan-super-league-2022-23?innings=1",

]

scroll_pause_time = 1

for url in urls:
  driver.get(url)
  time.sleep(5)
  screen_height = driver.execute_script("return window.screen.height;")
  i = 3
  while True:
    # try:
    #   driver.execute_script(f"window.scrollTo(0,{screen_height}*{i});".format(screen_height=screen_height, i=i))
    # except:
    #   i += 1
    #   time.sleep(scroll_pause_time)
    # scroll_height = driver.execute_script("return document.body.scrollHeight;")

    # if (screen_height) * i > scroll_height:
    #   break
    something = input("enter something")
    if something:
      break
  # req = Request(urls[0], headers={'User-Agent': 'Mozilla/5.0'})
  # page = urlopen(req)
  # html = page.read().decode('utf-8')
  soup = BeautifulSoup(driver.page_source, 'html.parser')



  espn_class_col_b = soup.find("div", class_="col-b")
  article_match_commentary = espn_class_col_b.find("div", class_="content match-commentary__content")
  article_match_commentary

  commentary_items_pre = article_match_commentary.find_all("div", class_="commentary-item pre ")
  commentary_items = article_match_commentary.find_all("div", class_="commentary-item ")
  commentary_items_end_of_over = article_match_commentary.find_all("div", class_="commentary-item end-of-over")
  testing = article_match_commentary.find_all("div", class_= r'commentary-item')

  len(commentary_items_end_of_over), len(commentary_items_pre), len(commentary_items), len(testing)

  ball_by_ball_outcome = {}

  over_pre = []
  score_pre = []
  comment_pre = []
  ball_description_pre = []
  for commentary_item_pre in testing:
    try:
      comment = commentary_item_pre.find("p", class_="comment").getText()
    except:
      comment = ""
    if not comment:
      comment = ""
    try:
      over = commentary_item_pre.find("div", class_="time-stamp").getText()
    except:
      over = 0
    print(over)
    try:
      score = commentary_item_pre.find("span", class_="over-score").getText()
    except:
      score = 0
    try:
      ball_description = commentary_item_pre.find("div", class_="description").getText()
    except:
      ball_description = ""

    over_pre.append(over)
    score_pre.append(score)
    comment_pre.append(comment)
    ball_description_pre.append(ball_description)

  len(over_pre), len(score_pre), len(ball_description_pre), len(comment_pre)

  

  commentary_pre_df = pd.DataFrame(list(zip(over_pre, score_pre, ball_description_pre, comment_pre)),
                columns =['Over', 'Score', 'Description', 'Comment'])

  commentary_pre_df

  over_not_pre = []
  score_not_pre = []
  comment_not_pre = []
  ball_description_not_pre = []
  for commentary_item in testing:
    comment = commentary_item.find("p", class_="comment")
    if not comment:
      comment = ""
    try:
      over = commentary_item.find("div", class_="time-stamp").getText()
    except:
      over = '0'
    try:
      score = commentary_item.find("span", class_="over-score").getText()
    except:
      score = '0'
    try:
      ball_description = commentary_item.find("div", class_="description").getText()
    except:
      ball_description = '-'

    over_not_pre.append(over)
    score_not_pre.append(score)
    comment_not_pre.append(comment)
    ball_description_not_pre.append(ball_description)

  len(over_not_pre), len(score_not_pre), len(ball_description_not_pre), len(comment_not_pre)

  commentary_not_pre_df = pd.DataFrame(list(zip(over_not_pre, score_not_pre, ball_description_not_pre, comment_not_pre)),
                columns =['Over', 'Score', 'Description', 'Comment'])

  commentary_not_pre_df

  over_final = []
  score_final = []
  ball_description_final = [] 
  comment_final = []

  over_pre

  i = 0
  j = 0

  over_not_pre.append(-1)
  over_pre.append(-1)
  over_not_pre
  while i < len(over_not_pre):                                              # 4 < 5 true
    while j < len(over_pre)-1:                                              # 3 < 4 true
      if float(over_not_pre[i]) > float(over_pre[j]):                                         # -1 > 5 false
        over_final.append(over_not_pre[i])                                      # append 6
        score_final.append(score_not_pre[i])
        ball_description_final.append(ball_description_not_pre[i])
        comment_final.append(comment_not_pre[i])
        print(over_final[-1])
        break
      elif float(over_not_pre[i]) <= float(over_pre[j]):                                     # -1 <= 5 true
        over_final.append(over_pre[j])                                          # append 5
        score_final.append(score_pre[j])
        ball_description_final.append(ball_description_pre[j])
        comment_final.append(comment_pre[j])
        print(over_final[-1])
        j = j + 1
      
    i = i + 1
      
  # print(len(over_final))
  # if i < len(over_not_pre):
  # 9, 9, 8,  7, 6, 6, 5

  print(len(over_final))

  final_df = pd.DataFrame(list(zip(over_final, score_final, ball_description_final, comment_final)),
                columns =['Over', 'Score', 'Description', 'Comment'])

  # final_df
  inn = ''
  if (url.split('/')[-1].split('-')[-1][-1]=='1'):
    inn = '2nd innings'
  else:
    inn = '1st innings'

  name = (" ").join(url.split('/')[-1].split('-')[:7])
  final_df.to_csv(name + " " + inn +".csv")

  # final_df.plot()
