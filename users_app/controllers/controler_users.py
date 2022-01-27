from unittest import result
from flask import redirect, render_template, request
from users_app import app 
from users_app.models.model_users import User

@app.route("/users",methods=['GET'])
def index():
    
    objects_user=User.get_all()
    return render_template("index.html", users = objects_user)


@app.route("/users/post",methods=['POST']) 
def create():
    
    nuevo_usuario={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    usuario_creado=User.create_new_user(nuevo_usuario)
    print("envio a la base de datos",usuario_creado)
    return redirect(f"/users/{usuario_creado}")


@app.route("/users/new",methods=['GET'])
def new_user():
    print("renderizando")
    return render_template("new_user.html")

@app.route("/users/<number>",methods=['GET'])
def show(number):
    numero_id = {
        "user_id":number
    }
    obj_user = User.get_user(numero_id)
    print("renderizando")
    return render_template("show_user.html", user=obj_user )

@app.route("/users/delete/<number>",methods=['GET'])
def delete(number):
    numero_id = {
        "user_id":number
    }
    obj_user = User.delete_user(numero_id)
    print(obj_user)
    return redirect ("/users")

@app.route("/users/<number>/edit",methods=['GET','POST'])
def edit_user(number):
    if request.method == 'GET':
        numero_id = {
            "user_id":number
        }
        obj_user = User.get_user(numero_id)
        return render_template("edit.html",user=obj_user)
    
    if request.method == 'POST':
        data = {
            "id":number,
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"],
        }
        result = User.edit_user(data)
        print(result)
        return redirect(f"/users/{number}")