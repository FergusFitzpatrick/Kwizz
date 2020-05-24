from flask import Flask, request, render_template

app = Flask(__name__)

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
