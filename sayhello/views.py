# -*- coding:utf-8 -*-
"""
   author:wnl
   date:2018-12-7
"""

from flask import flash,redirect,url_for,render_template
from sayhello import db,app
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    #加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body,name=name) #实例化模型，创建记录
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world')
        return redirect(url_for('index')) #重定向视图
    return render_template('index.html',form=form,messages=messages)
    
