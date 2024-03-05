from flask import Blueprint, request, jsonify, session
from models import Note,User,db

notes_blueprint = Blueprint('notes', __name__)

@notes_blueprint.route('/add_note', methods=['POST'])
def add_note():
    if 'username' in session:
        data = request.get_json()
        note_text = data.get('note_text')

        user = User.query.filter_by(username=session['username']).first()
        new_note = Note(text=note_text, user=user)
        db.session.add(new_note)
        db.session.commit()

        return jsonify({'message': 'Note added successfully'})
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@notes_blueprint.route('/get_notes')
def get_notes():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        notes = Note.query.filter_by(user=user).all()

        return jsonify({'notes': [note.text for note in notes]})
    else:
        return jsonify({'error': 'Unauthorized'}), 401
