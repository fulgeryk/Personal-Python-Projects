import datetime
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import now
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean, DateTime
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)

class ToDoForm(FlaskForm):
    title = StringField("ToDo Task", validators=[DataRequired()])
    submit = SubmitField("Submit")

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#Configure TABLES
class ToDoBase(db.Model):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/", methods = ["GET"])
def home():
    form = ToDoForm()
    result = db.session.execute(db.select(ToDoBase))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, form=form)

@app.route("/add", methods = ["POST"])
def add():
    form = ToDoForm()
    if form.validate_on_submit():
        new_task = ToDoBase(
            title = form.title.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    return redirect(url_for("home"))

@app.route("/toggle/<int:id>", methods = ["POST"])
def toggle(id):
    requested_toggle = db.get_or_404(ToDoBase, id)
    requested_toggle.done = not requested_toggle.done
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>", methods = ["POST"])
def delete(id):
    requested_delete =db.get_or_404(ToDoBase, id)
    db.session.delete(requested_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)