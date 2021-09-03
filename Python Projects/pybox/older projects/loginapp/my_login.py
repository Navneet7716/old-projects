from flask import Flask, request, render_template,url_for,redirect


app=Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


data = ["navneetsingh969@gmail.com","dhruvrishi123"]

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/more", methods = ["POST", "GET"])
def more():
		if request.method == "POST":
			if request.form.get("email") == data[0] and request.form.get("password") == data[1]:
				return render_template("more.html")
			else:
				return render_template("home.html")
				



if __name__ == '__main__':
	app.run(debug=True)