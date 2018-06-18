import urllib.request
from bs4 import BeautifulSoup
import re

def parseAnswer(questionid, answerid):
	html = urllib.request.urlopen("https://www.zhihu.com/question/" + questionid + "/answer/" + answerid).read()
	soup = BeautifulSoup(html, "lxml")
	answer = ''
	for i in soup.find_all('p'):
		answer = answer + str(i.string) + '\n'
	return(answer)

def getAnswers(questionid, page):
	answerlist = []
	answersjson = str(urllib.request.urlopen("https://www.zhihu.com/api/v4/questions/" + questionid + "/answers?sort_by=default&limit=20&offset=" + page).read())
	for i in re.findall("http://www.zhihu.com/api/v4/answers/\d+\"", answersjson):
		answerlist.append(i[36:-1])
	return(answerlist)
