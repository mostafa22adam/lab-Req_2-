from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")


@app.route('/submit' , methods = ["POST"])
def submit():
    name = request.form['name']
    age = request.form['age']
    height = request.form['height']

    return render_template("result.html" , name=name , age=age, height=height)

if __name__ == '__main__':
    app.run(debug=True)

