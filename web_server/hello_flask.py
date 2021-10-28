from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
	now = datetime.datetime.now()
	time_string = now.strftime("%Y-%m-%d %H:%M")
	template_data = {
		'title':"Hello!",
		'time':time_string,
	}
	return render_template('main.html', **template_data)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)


