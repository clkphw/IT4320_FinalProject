from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *

def loginAdmin(username,psw):
    adminFile = open('./passcodes.txt')
    for admin in adminFile.readlines():
        admin = admin.split(',')
        user = admin[0].strip()
        password = admin[1].strip()
        if (user == username) and (password == psw):
            return True
    return False

#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")



        if loginAdmin(username, password):
            form = ReservationForm()
            return render_template("reservations.html", form=form, template="form-template")
        else:
            form = UserOptionForm()
            return render_template("options.html", form=form, template="form-template")
    
    return render_template("admin.html", form=form, template="form-template")    

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

