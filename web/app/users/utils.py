import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail


def save_picture(form_picture, current_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    prev_picture = os.path.join(current_app.root_path, 'static/profile_pics', current_pic)
    if os.path.exists(prev_picture) and 'default' not in prev_picture:
        os.remove(prev_picture)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='noreply@dunedin.kiwi', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}
    If you did not make this request, please ignore this email.
    '''
    mail.send(msg)
