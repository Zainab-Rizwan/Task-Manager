from app import app
#app instance
from flask import render_template

import forms

#routes
@app.route('/')
@app.route('/index')
#decorator to function
def index():
    return render_template('index.html', current_title='custom title')

@app.route('/about', methods=['GET','POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about.html', form= form, title=form.title.data)
    return render_template('about.html', form=form)