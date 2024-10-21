from flask import url_for, redirect, render_template, flash
from sayhello import app, db

from sayhello.models import Message
from sayhello.forms import HelloForm
@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all() #查询全部记录，按照timestamp降序排列
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index_boot.html', form=form , messages=messages)