from flask import Flask, request, render_template

app = Flask(__name__)   # sign the contract: the app belongs to me

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        # shoule be the same name of <p><input type="number" step="0.01" name="rate"></p> (from index.html)
        # POST: I'm waiting for the data, then I post the res(prediction)
        return(render_template("index.html", result=90.2 + (-50.6*rate)))
    else:
        return(render_template("index.html", result="waiting for exchange rate ..."))
    
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80)
    # If can't work, check the host and port number.