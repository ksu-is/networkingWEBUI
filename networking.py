import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/dnslookup')
def dnslookup():
	return render_template("dnslookup.html")

@app.route('/hostlist', methods = ['GET', 'POST'])
def hostlist():
	while request.form.get('submit') == None:
		return render_template("hostlist.html")
	else:
		hostlist=os.popen("arp -a")
		output=hostlist.read()
		print(output)
		return render_template("hostlist.html", output=output)

@app.route('/pinghost', methods = ['GET', 'POST'])
def pinghost():
	while request.form.get('ping') == None:
		return render_template("pinghost.html")
	else:
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


@app.route("/traceroute", methods = ['GET', 'POST'])
def traceroute():
	while request.form.get('trace') == None:
		return render_template("traceroute.html")
	else:
		trace = request.form.get('trace')
		traceroute=os.popen('tracert -h 10 {}'.format(trace))
		output=traceroute.read()
		print(output)
		return render_template("traceroute.html", output=output)
	
if __name__ == "__main__":
	app.run(debug=True)






