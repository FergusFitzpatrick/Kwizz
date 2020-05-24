import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("questions.csv")
    reader = csv.reader(f)
    for id,name,answer,fakeanswer1,fakeanswer2,fakeanswer3,category,image in reader:
		db.execute("INSERT INTO questions (id, name, answer, fakeanswer1, fakeanswer2, fakeanswer3, category, image) VALUES (:id, :name, :answer, :fakeanswer1, :fakeanswer2, :fakeanswer3, :category, :image)",
			{"id": id, "name": name, "answer": answer, "fakeanswer1": fakeanswer1, "fakeanswer2": fakeanswer2, "fakeanswer3": fakeanswer3, "category": category, "image": image})

@app.route('/')
def index():
	title = "Home Page"
	return render_template("index.html", title=title)

@app.route('/quizStart')
def quizStart():
	title = "Let's Start!"
	return render_template("quizstart.html", title=title)

@app.route('/quiz', methods=['POST'])
def quiz():
	name = request.form.get('name')
	category = request.form.get('category')
	return render_template("quiztemplate.html", name=name, category=category)


if __name__ == '__main__':
	app.run(debug=True)
