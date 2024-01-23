from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('main.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us.html', name='Maria')


if __name__ == '__main__':
    app.run(debug=True)
