from flask import Flask, render_template, redirect, request
from parser import parseAnswer, getAnswers
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		return  redirect("/q/" + request.form['qid'] + '/p/1')

@app.route("/q/<questionid>/p/<int:page>")
def question(questionid, page):
	answerList = getAnswers(questionid, str(page*20))
	return render_template('question.html', questionid = questionid, answers = answerList)
	
@app.route("/q/<questionid>/a/<answerid>")
def answer(questionid, answerid):
	answer = parseAnswer(questionid, answerid)
	return render_template('answer.html', answer = answer)

if __name__=='__main__':
	from werkzeug.contrib.fixers import ProxyFix
	app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
