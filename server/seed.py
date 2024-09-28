#!/usr/bin/env python3

from app import app

from models import db, Workouts

from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Creating Workouts")
        pushup = Workouts(name = "Pushup", category_id = "Chest", description = "A push-up is a calisthenic exercise that involves raising and lowering the body while lying face down by bending and straightening the arms.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        barbell_bench_press = Workouts(name = "Barbell bench press", category_id = "Chest", description = "A weightlifting exercise that involves lying on a bench and pushing a weight upward using your hands.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        incline_bench_press = Workouts(name = "Incline bench press", category_id = "Chest", description = "It's performed on an incline bench that's usually set at a 30–45 degree angle, targeting the upper chest.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        machine_flye = Workouts(name = "Machine flye", category_id = "Chest", description = "An upper body strength training exercise that targets the chest, deltoids, and triceps.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        smith_machine_bench_press = Workouts(name = "Smith machine bench press", category_id = "Chest", description = "a compound exercise that uses a Smith machine and a bench to press a barbell above you.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        incline_smith_machine_bench_press = Workouts(name = "Incline smith machine bench press", category_id = "Chest", description = "Preformed on an incline bench set at a 30-45 degree angle targeting the upper chest on a smith machine",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        dumbell_incline_bench_press = Workouts(name = "Dumbbell incline bench press", category_id = "Chest", description = "An upper body exercise that targets the chest, shoulders, and triceps.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        dumbell_bench_press = Workouts(name = "Dumbbell bench press", category_id = "Chest", description = "An upper-body exercise that uses dumbbells and a bench to target the chest, shoulders, and arms.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        dumbell_incline_flye = Workouts(name = "Dumbbell incline flye", category_id = "Chest", description = "The dumbbell incline fly, also known as the incline chest fly or incline pec fly, is an exercise that works the chest, anterior deltoids, and biceps.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        cable_lower_chest_raise = Workouts(name = "Cable lower chest raise", category_id = "Chest", description = "A cable lower chest raise is a strength exercise that involves using a low pulley cable machine to squeeze your lower chest",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        cable_upper_chest_raise = Workouts(name = "Cable upper chest raise", category_id = "Chest", description = "Cable upper chest exercises can target different parts of the chest by adjusting the cable height and your arm position",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        machine_incline_chest_press = Workouts(name = "Machine incline chest press", category_id = "Chest", description = "a compound exercise that targets the upper chest, front shoulders, back of the arms, and serratus anterior.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")
        dumbell_pullover = Workouts(name = "Dumbbell pullover", category_id = "Chest", description = "a weightlifting exercise that works the chest, shoulders, back, and abs.",video_url = "https://www.youtube.com/watch?v=mm6_WcoCVTA")


        db.session.commit()

        print("Seeding complete!")
