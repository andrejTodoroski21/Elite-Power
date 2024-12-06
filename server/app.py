import os
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt


from models import db, User, Workouts, Program, Category

app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

# bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)

# get one workout from the database
@app.get("/api/workouts/<string:workout_name>")
def get_workout(workout_name):
    workout = Workouts.query.filter_by(name=workout_name).first()
    if workout:
        return workout.to_dict(), 200
    return {"message": "Workout not found"}, 404

# get all workouts from the database
@app.get("/api/workouts")
def get_all_workouts():
    return [i.to_dict() for i in Workouts.query.all()], 200

@app.get("/api/workouts/category/<int:category_id>")
def get_workouts_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return {"message": "Category not found"}, 404
    workouts = Workouts.query.filter_by(category_id=category_id).all()
    return [workout.to_dict() for workout in workouts], 200

# Get all categories (for the dropdown)
@app.get("/api/categories")
def get_categories():
    categories = Category.query.all()
    return [category.to_dict() for category in categories], 200

        
if __name__ == '__main__':
    app.run(port=5555, debug=True)
