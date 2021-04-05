from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/dnslookup")
def dnslookup():
	return render_template("dnslookup.html")

@app.route("/hostlist")
def hostlist():
	return render_template("hostlist.html")

@app.route("/pinghost")
def pinghost():
	return render_template("pinghost.html")

@app.route("/scannetwork")
def scannetwork():
	return render_template("scannetwork.html")

@app.route("/tcpdump")
def tcpdump():
	return render_template("tcpdump.html")

@app.route("/traceroute")
def traceroute():
	return render_template("traceroute.html")

if __name__ == "__main__":
	app.run(debug=True)


