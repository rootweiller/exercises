from flask import Flask, render_template

# Create Application Object

app = Flask(__name__)


# Use decorators to link the function to a url
@app.route('/')
def home():

	return "Hello World!"

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


if __name__ == '__main__':
	app.run(debug=True)