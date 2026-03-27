from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from . import db
from .models import User, Message

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('register.html')


@main.route('/chat', methods=['GET','POST'])
def chat():

    if request.method == 'POST':
        sender = request.form['sender']
        receiver = request.form['receiver']
        content = request.form['message']

        # Bloquer l'envoi à soi-même
        if sender == receiver:
            messages = _get_formatted_messages()
            users = User.query.all()
            return render_template(
                'chat.html',
                messages=messages,
                users=users,
                current_user=session.get('username', users[0].username if users else ""),
                error="Vous ne pouvez pas vous envoyer un message à vous-même."
            )

        sender_user = User.query.filter_by(username=sender).first()
        receiver_user = User.query.filter_by(username=receiver).first()

        if sender_user and receiver_user:
            msg = Message(
                sender_id=sender_user.id,
                receiver_id=receiver_user.id,
                content=content
            )
            db.session.add(msg)
            db.session.commit()

    messages = _get_formatted_messages()
    users = User.query.all()

    return render_template(
        'chat.html',
        messages=messages,
        users=users,
        current_user=session.get('username', users[0].username if users else "")
    )


def _get_formatted_messages():
    messages = Message.query.all()
    formatted_messages = []
    for m in messages:
        sender = User.query.get(m.sender_id)
        receiver = User.query.get(m.receiver_id)
        formatted_messages.append({
            'sender': sender.username,
            'receiver': receiver.username,
            'content': m.content,
            'timestamp': m.timestamp
        })
    return formatted_messages


@main.route('/monitor')
def monitor():
    users_count = User.query.count()
    messages_count = Message.query.count()
    return render_template('monitor.html', users_count=users_count, messages_count=messages_count)


@main.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['username'] = user.username
            return redirect(url_for('main.chat'))
        else:
            return "Utilisateur ou mot de passe incorrect"

    return render_template('login.html')
