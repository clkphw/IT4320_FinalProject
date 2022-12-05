from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *


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

    return render_template("admin.html", form=form, template="form-template",title=title, ResList=ResList)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    
    form = ReservationForm()
    return render_template("reservations.html", form=form, template="form-template", title=title, ResList=ResList)


