from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()

    return ' '.join(soup.stripped_strings)
df = pd.read_csv('Participant_Details.csv')
df1 = df[['url', 'name','email']]
saved_column = df.url
paragraphs = ""
name=[]
badges=[]
email=[]
completed_all=[]
score=[]

kotlin_basics=[]
funct=[]
classes_objects=[]
build_app=[]
layouts=[]
app_navigation=[]

for v,w,z in zip(df1.url,df1.name,df1.email):
    paragraphs=""

    kotlin_basics_s = "No"
    funct_s = "No"
    classes_objects_s = "No"
    build_app_s = "No"
    layouts_s = "No"
    app_navigation_s = "No"
    completed_all_s = "No"
    score_s = 0
    
    options = Options()
    options.headless = True
    wd = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    responce = wd.get(v)
    name.append(w)
    email.append(z)
    time.sleep(8)  
    soup = BeautifulSoup(wd.page_source, 'lxml')
    div = soup.find_all('div', {'class':'badge-title'})
    badgelist=""
    for x in div:
        badgelist=remove_tags(str(x))+", "+badgelist
        paragraphs=paragraphs+(str(x))
    if "Lesson 1: Kotlin Basics" in paragraphs:
        kotlin_basics_s="Yes"
        score_s+=1
    if "Lesson 2: Functions" in paragraphs:
        funct_s="Yes"
        score_s+=1
    if "Lesson 3: Classes and Objects" in paragraphs:
        classes_objects_s="Yes"
        score_s+=1
    if "Lesson 4: Build your first Android app" in paragraphs:
        build_app_s="Yes"
        score_s+=1
    if "Lesson 5: Layouts" in paragraphs:
        layouts_s="Yes"
        score_s+=1
    if "Lesson 6: App navigation" in paragraphs:
        app_navigation_s="Yes"
        score_s+=1

    kotlin_basics.append(kotlin_basics_s)
    funct.append(funct_s)
    classes_objects.append(classes_objects_s)
    build_app.append(build_app_s)
    layouts.append(layouts_s)
    app_navigation.append(app_navigation_s)
    if score == 6:
        completed_all_s="Yes"

    score.append(score_s)
    completed_all.append(completed_all_s)
    paragraphs = paragraphs + "<br><br>"
    badges.append(badgelist)

dict = {'Name': name,'Email':email, 'Badges': badges, 'Kotlin Basics':kotlin_basics, 'Functions':funct, 'Classes and Objects':classes_objects, 'Build your first Android app':build_app, 'Layouts':layouts, 'App navigation':app_navigation, 'Score Out of 6':score,'Completed All Badges':completed_all}
df = pd.DataFrame(dict)
df.to_csv('Participant_Completion.csv')
paragraphs=remove_tags(paragraphs)