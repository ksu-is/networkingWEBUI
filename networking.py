import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/dnslookup')
def dnslookup():
	return render_template("dnslookup.html")

@app.route('/hostlist')
def hostlist():
	hostlist=os.popen("arp -a")
	output=hostlist.read()
	print(output)
	return render_template("hostlist.html", output=output)

@app.route('/pinghost', methods = ['GET', 'POST'])
def pinghost():
	ping = request.form.get('ping')
	hostping=os.popen('ping -n 10 {} -w 5'.format(ping))
	output=hostping.read()
	print(output)
	return render_template("pinghost.html", output=output)

@app.route('/scannetwork', methods = ['GET', 'POST'])
def scannetwork():
	scan = request.form.get('scan')
	portscan=os.popen('nmap {}'.format(scan))
	output=portscan.read()
	print(output)
	return render_template("scannetwork.html", output=output)
	
@app.route('/tcpdump')
def tcpdump():
	return render_template("tcpdump.html")


@app.route("/traceroute")
def traceroute():
	return render_template("traceroute.html")

if __name__ == "__main__":
	app.run(debug=True)






