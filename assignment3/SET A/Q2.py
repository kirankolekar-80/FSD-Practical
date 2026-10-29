from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    return "Name: Kiran Kolekar<br>Roll No: 40"

if __name__ == '__main__':
    app.run(debug=True)