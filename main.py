from flask import Flask, render_template
from parser import parseAnswer, getAnswers
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/q/<questionid>/p/<page>")
def question(questionid, page):
	answerList = getAnswers(questionid, page)
	return render_template('question.html', questionid = questionid, answers = answerList)
	
@app.route("/q/<questionid>/a/<answerid>")
def answer(questionid, answerid):
	answer = parseAnswer(questionid, answerid)
	return render_template('answer.html', answer = answer)

if __name__=='__main__':
	from werkzeug.contrib.fixers import ProxyFix
	app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
