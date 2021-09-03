from flask import Flask, session, request, url_for, render_template

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

notes = []

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == 'GET':
        notes.clear()
    if request.method == 'POST':
        note = request.form.get("note")
        if note == "":
            url_for('home')
        else:
            notes.append(note)
    return render_template("home.html", notes=notes)


    
if __name__ == '__main__':
    app.run(debug=True)