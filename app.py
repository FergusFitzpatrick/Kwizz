import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('postgresql://ferguspatrick:tiger@localhost:5432/Kwizz')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)


@app.route('/')
def index():
	title = "Home Page"
	return render_template("index.html", title=title)

@app.route('/quizStart')
def quizStart():
	title = "Let's Start!"
	return render_template("quizstart.html", title=title)

@app.route('/initQuiz', methods=['POST', 'GET'])
def initQuiz():
    count = 1
    title = (f"Q. {count}")
    name = request.form.get('name')
    category = request.form.get('category')
    record = db.execute("SELECT * FROM questions").fetchone()
    return render_template("quiztemplate.html", title=title, record=record, name=name, category=category)


if __name__ == '__main__':
	app.run(debug=True)
