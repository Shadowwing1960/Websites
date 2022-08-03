from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)
  
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/notepad')
def notepad():
    # Specific path
    path = 'C:/Users/HP Admin/PycharmProjects/Website/Notes/Notes_Code'
    sys.path.insert(0, path)

    # importing function
    from Notes.Note_Pad_Code.Note_Pad import note_pad
   
    # Running Gui Note Pad
    note_pad()
    return redirect(url_for('/'))
  
@views.route('/todolist', methods=['GET', 'POST'])
def to_do_list():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Task is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Task added!', category='success')

    return render_template("to_do_list.html", user=current_user)

