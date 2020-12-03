from flask import render_template, request 
from app import app
from app.models.event_list import *
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title='Home ', events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    date = request.form['event_date']
    split_date = date.split('-')

# def Convert(string): 
#     li = list(string.split("-")) 
#     return li 

# ---- Keith's slack suggestion below ----
# date = request.form['event_date']
# split_date = date.split('-')
# date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
# ----------------------------------------

    # my_date = datetime.strptime(request.form['event_date'], "%Y-%M-%D")
    
    event_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form['name']
    event_guests = request.form['number_of_guests']
    event_location = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)