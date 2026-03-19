from flask import Blueprint, request, jsonify
from . import db
from .models import User, Message

api = Blueprint('api', __name__)

@api.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    sender_name = data.get('sender')
    receiver_name = data.get('receiver')
    content = data.get('content')
    sender = User.query.filter_by(username=sender_name).first()
    receiver = User.query.filter_by(username=receiver_name).first()
    if sender and receiver:
        msg = Message(sender_id=sender.id, receiver_id=receiver.id, content=content)
        db.session.add(msg)
        db.session.commit()
        return jsonify({'status':'successful'}), 200
    return jsonify({'status':'error'}), 400

@api.route('/messages/<username>', methods=['GET'])
def get_messages(username):
    user = User.query.filter_by(username=username).first()
    if user:
        msgs = Message.query.filter((Message.sender_id==user.id)|(Message.receiver_id==user.id)).all()
        result = [{'sender': User.query.get(m.sender_id).username,
                   'receiver': User.query.get(m.receiver_id).username,
                   'content': m.content,
                   'timestamp': m.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for m in msgs]
        return jsonify(result), 200
    return jsonify([]), 404