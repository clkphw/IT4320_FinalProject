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

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

#BRADINS CODE
def CostAdmin(seatchart):
    costchart = get_cost_matrix()

    total = 0
    for x in range(len(seatchart)):
        for i in range(4):
            if(seatchart[x][i]=="X"):
                total += costchart[x][i]

    return "Total cost: " + str(total)
    

def loadreservations():
    f = open("reservations.txt", "r")
    chart = [
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],

        ]
    for i in f:
        #print(i.split(",")[1],i.split(",")[2])
        x = int(i.split(",")[1])
        y = int(i.split(",")[2])
        chart[x][y] = "X"
    return chart

def addreservations(firstname, row, col):
    
    f = open("reservations.txt", "w")
    inputxt = firstname + "," + row + "," + col + "\n"
    f.write(inputxt)
    f.close
    loadreservations()
    return "worked"
    
#title = ("Seating Chart")
#ResList = loadreservations()
#total = CostAdmin()

#BRADINS CODE

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
            form = AdminLoginForm()
            title = ("Printing Seating Chart...")
            ResList = loadreservations()
            total = CostAdmin(ResList)
            return render_template("admin.html", form=form, template="form-template", title=title, ResList=ResList,total=total)
        else:
            form = AdminLoginForm()
            error_msg = "Bad Username/Password Combination. Try Again."
            return render_template("admin.html", error=error_msg, form=form, template="form-template")
    
    return render_template("admin.html", form=form, template="form-template")    

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()
    title = ("Seating Chart")
    ResList = loadreservations()
    return render_template("reservations.html", form=form, template="form-template", title=title, ResList=ResList)

