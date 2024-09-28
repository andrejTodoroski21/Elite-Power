from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Workouts(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    videourl = db.Column(db.String, nullable=False)

    # Category relationship
    category = db.relationship("Category", back_populates="workouts")

    __serialize_rules__ = ('-id', '-category_id', 'name', 'description', 'video_url', 'category')

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

    # Relationship to the Workouts model
    programs = db.relationship("Programs", back_populates="user", cascade="all, delete-orphan")

    __serialize_rules__ = ('-password', 'first_name', 'last_name', 'email', 'programs')

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)

    workouts = db.relationship("Workouts", back_populates="catergory")

class Program(db.Model, SerializerMixin):
    __tablename__ = "programs"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    name = db.Column(db.String(50),  nullable = False)

    user = db.relationship("User", back_populates="programs")
    program_workouts = db.relationship("ProgramWorkout", back_populates = "program", cascade = "all, delete-orphan")

    __serialize_rules__ = ('-user_id', 'name', 'program_workouts')

class ProgramWorkout(db.Model, SerializerMixin):
    __tablename__ = "program_workouts"

    id = db.Column(db.Integer, primary_key = True)
    program_id = db.Column(db.Integer, db.ForeignKey("programs.id"), nullable = False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable = False)
    sets = db.Column(db.Integer, nullable = False)
    reps = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Float, nullable = False)

    program = db.relationship("Program", back_populates = "program_workouts")
    workout = db.relationship("Workout")

    __serialize_rules__ = ('-id', '-program_id', 'reps', 'sets', 'weight')


