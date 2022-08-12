from flask import Blueprint, render_template, request, flash
from flask import jsonify, redirect, url_for
from flask_login import login_required, current_user
from Website.models import Note
from Website import db
import json
import threading
import sys

views = Blueprint('views', __name__)


# Home URL
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


# Deleting a note from To Do List URl
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Task Removed', category='success')

    return jsonify({})


# Open GUI Note Pad in website as a URL
@views.route('/notepad')
def notepad():
    def redirect_home():
        redirect(url_for('/'))

    # Specific path
    path = 'C:/Users/HP Admin/PycharmProjects/Website/Notes/Notes_Code'
    sys.path.insert(0, path)

    # importing function
    from Notes.Note_Pad_Code.Note_Pad import note_pad
    notes = threading.Thread(target=note_pad, name='notes')
    redirecting = threading.Thread(target=redirect_home, name='redirecting')

    # Running Gui Note Pad
    redirecting.start()
    notes.start()
    flash('Note Pad Opened', category='success')
    return render_template("home.html", user=current_user)


# To do list URL
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


# Contact us URl
@views.route('/contact-us', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html", user=current_user)
