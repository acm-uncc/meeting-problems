import flask

app = flask.Flask(__name__)

meetings = {}
meeting_id = 0

@app.post("/meetings")
def submit_meeting():
	global meeting_id

	id_ = meeting_id

	meeting_id += 1
	meetings[id_] = (
		flask.request.form["topic"],
		flask.request.form["date"],
		flask.request.form["time"]
	)

	return flask.redirect(flask.url_for("list_meetings"))

@app.route("/meetings")
def list_meetings():
	return flask.render_template("meetings.html", meetings=meetings)

@app.route("/meetings/add")
def add_meeting():
	return flask.render_template("add_meeting.html")

@app.post("/meetings/delete")
def delete_meeting():
	pass
