from flask import Flask, render_template, request, url_for, flash, redirect
from tkinter import *
from tkinter import messagebox
app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('./project1')
print('Connected to Database')

def myFun():
   top = Tk()
   top.geometry("100x100")
   messagebox.showinfo("informatio1n", "Information1")
   top.mainloop()

def myFun2():
   top = Tk()
   top.geometry("100x100")
   messagebox.showinfo("information2", "Information2")
   top.mainloop()


@app.route('/',methods=('GET', 'POST'))
def index():
   if request.method == "POST":
      myFun()
   return render_template('index.html')

@app.route('/aboutus',methods=('GET', 'POST'))
def aboutus():
   if request.method == "POST":
      myFun()
   return render_template('aboutus.html')


@app.route('/login',methods=('GET', 'POST'))
def login():
   import sqlite3 as sql
   con = sql.connect("./project1.db")
   if request.method == "POST":
      if request.form['submit'] == 'Sign In':
         username = request.form['username']
         password = request.form['password']
         cur = con.cursor()
         statement = f"SELECT email from users WHERE email='{username}' AND password = '{password}';"
         cur.execute(statement)
         if not cur.fetchone():  # An empty result evaluates to False.
            return render_template('login.html')
         else:
            return render_template('admin.html')
   else:
      return render_template('login.html')

@app.route('/signup',methods=('GET', 'POST'))
def signup():
   import sqlite3
   conn = sqlite3.connect('./project1.db')
   if request.method == "POST":
      if request.form['register'] == 'Register':
         name = request.form['name']
         email = request.form['email']
         password1 = request.form['password']
         password2 = request.form['confirmpassword']
         if password1 == password2:
            conn.execute("INSERT INTO users (name,email,password) VALUES ('"+name+"','"+email+"', '"+password1+"')")
            conn.commit()
            print("SignUp successfully")
            conn.close()
            return render_template('login.html')
         else:
            print('Please enter valid password.')
            return render_template('signup.html')
   else:
      return render_template('signup.html')


@app.route('/contactus',methods=('GET', 'POST'))
def contactus():
   if request.method == "POST":
      myFun()
   return render_template('contactus.html')

@app.route('/admin',methods=('GET', 'POST'))
def admin():
   if request.method == "POST":
      if request.form['submit_button'] == "Mask Detection":
         myFun()
      elif request.form['submit_button'] == "Social Distance":
         myFun2()
   return render_template('admin.html')



if __name__ == '__main__':
   app.run(debug = True)