from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("survey.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/submitted', methods=['POST']) #
def create_user():
    print("Got Post Info")
    # # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['name']
    location = request.form['location']
    lang = request.form['coding_language']
    comment = request.form['comment']
    # # redirects back to the '/' route
    return render_template("code.html",name=name,location=location,lang=lang,comment=comment)
@app.route('/danger')
def back():
    print("STAY OUT")
    return redirect('/')
if (__name__=="__main__"):
    # run our server
    app.run(debug=True)