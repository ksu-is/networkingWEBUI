import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
	return render_template("login.html")

@app.route('/index')
def home():
	return render_template("index.html")

@app.route('/dnslookup', methods = ['GET', 'POST'])
def dnslookup():
	if request.form.get('dns') == None:
		return render_template("dnslookup.html")
	else:
		dns = request.form.get('dns')
		dnslookup=os.popen('nslookup {}'.format(dns))
		output=dnslookup.read()
		print(output)
	return render_template("dnslookup.html", output=output)

@app.route('/hostlist', methods = ['GET', 'POST'])
def hostlist():
	if request.form.get('submit') == None:
		return render_template("hostlist.html")
	else:
		hostlist=os.popen("arp -a")
		output=hostlist.read()
		print(output)
		return render_template("hostlist.html", output=output)

@app.route('/pinghost', methods = ['GET', 'POST'])
def pinghost():
	if request.form.get('ping') == None:
		return render_template("pinghost.html")
	else:
		ping = request.form.get('ping')
		hostping=os.popen('ping -n 10 {} -w 5'.format(ping))
		output=hostping.read()
		print(output)
		return render_template("pinghost.html", output=output)

@app.route('/scannetwork', methods = ['GET', 'POST'])
def scannetwork():
	if request.form.get('scan') == None:
		return render_template("scannetwork.html")
	else:
		scan = request.form.get('scan')
		portscan=os.popen('nmap {}'.format(scan))
		output=portscan.read()
		print(output)
		return render_template("scannetwork.html", output=output)
	
@app.route('/tcpdump')
def tcpdump():
	return render_template("tcpdump.html")


@app.route("/traceroute", methods = ['GET', 'POST'])
def traceroute():
	if request.form.get('trace') == None:
		return render_template("traceroute.html")
	else:
		trace = request.form.get('trace')
		traceroute=os.popen('tracert -h 10 {}'.format(trace))
		output=traceroute.read()
		print(output)
		return render_template("traceroute.html", output=output)
	
if __name__ == "__main__":
	app.run(debug=True)






