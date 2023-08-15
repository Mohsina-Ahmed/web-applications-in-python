import os
from flask import Flask, request, Response

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

#Challenge
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"

#using POST
@app.route("/hello", methods=['GET'])
def hello():
    name = request.args['name']
    return f"Hello {name}"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    return f"Goodbye {name}!"

@app.route('/introduction', methods =['POST'])
def introduction():
    name = request.form['name']
    meet = request.form['meet']
    return f"Hi {name}! I would like to introduce you to {meet}"

@app.route('/submit', methods =['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']
    count=0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in text:
        if letter in vowels:
            count+=1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods = ['POST'])
def sort_names():
    
    if 'names' not in request.form:
        return "Please provide a list of strings (comma-seperated)", 400
    names = request.form['names']
    # if names == '':
    #     return Response("Please provide a list of strings (comma-seperated)", status = 400)
    #print(text)
    name_as_list = names.split(",")
    name_as_list.sort()
    name_as_string = (",").join(name_as_list)
    return name_as_string

@app.route('/add-names', methods = ['POST'])
def add_names(): 
    new_name = 'Mohsina'
    new_list_sorted = sorted((request.form['names']+','+new_name).split(','))
    return ','.join(new_list_sorted) 




# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

