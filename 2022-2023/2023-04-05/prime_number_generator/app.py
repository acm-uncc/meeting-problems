import flask

app = flask.Flask(__name__)

def compute_primes(n):
	primes = []

	for i in range(2, n):
		is_prime = True

		for j in range(2, i):
			if i % j == 0:
				is_prime = False

				break

		if is_prime:
			primes.append(i)

	return primes

@app.route("/primes")
def index():
	n = int(flask.request.args["n"])

	return flask.render_template("index.html", primes=compute_primes(n))
