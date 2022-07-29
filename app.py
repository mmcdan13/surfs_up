# import dependencies

from flask import Flask

# create a new Flask instance called "app"
# "__name__" denotes the name of the current function

app = Flask(__name__)

#Define the root (aka starting point)
#the forward slash is the highest level of hierarchy in
#any computer system

@app.route('/')
def hello_world():
    return 'Hello world'