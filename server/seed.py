#!/usr/bin/env python3

from app import app

from models import db, Workouts

from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Creating Workouts")
        #chest exercises 
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

        #bicep exercises
        dumbbell_bicep_curl = Workouts(name = "Dumbbell bicep curl", category_id = "Bicep", description = "hold a dumbbell with your palm facing upward. Slowly curl the weight up by bending your elbow, keeping your elbow close to your body. Then slowly lower the weight to the starting position.", video_url = "")
        barbell_preacher_curl = Workouts(name = "Barbell preacher curl", category_id = "Bicep", description = "a bicep exercise that isolates the biceps and is performed on a preacher bench.", video_url = "")
        preacher_curl_machine = Workouts(name = "Preacher curl machine", category_id = "Bicep", description = "a piece of exercise equipment that allows you to isolate your biceps by performing curls while seated on an angled bench.", video_url = "")
        ez_bar_curl = Workouts(name = "EZ bar curl", category_id = "Bicep", description = "a multi-angled barbell whose design focuses on working your triceps and biceps while helping to reduce pressure and stress from your elbows and wrist.", video_url = "")
        barbell_curl = Workouts(name = "Barbell curl", category_id = "Bicep", description = "A barbell curl is a variation of the biceps curl that uses a weighted barbell.", video_url = "")

        #Leg exercise
        barbell_back_squat = Workouts(name = "Barbell back Squat", category_id = "Leg", description = "a compound exercise that activates the lower body's muscles, including the hamstrings, glutes, and lower back.", video_url = "")
        machine_leg_extension = Workouts(name = "Machine leg extension", category_id = "Leg", description = "a lever machine designed to isolate your quads by doing a knee extension with weights.", video_url = "")
        leg_press = Workouts(name = "Leg press", category_id = "Leg", description = "a seated exercise that uses a weighted platform to work the lower body muscles.", video_url = "")
        lying_leg_curl = Workouts(name = "Lying leg curl", category_id = "Leg", description = "an exercise that strengthens the hamstrings and glutes while keeping the upper body still.", video_url = "")

        #back exercises 
        lat_pulldown = Workouts(name = "Lat pulldown", category_id = "Back", description = "a popular exercise that strengthens the upper body and back muscles.", video_url = "")
        barbell_bent_over_row = Workouts(name = "Barbell bent over row", category_id = "Back", description = "a compound exercise that works muscles in both the upper and lower body.", video_url = "")
        pullup = Workouts(name = "Pullup", category_id = "Back", description = "a challenging upper-body exercise that involves gripping a bar and pulling yourself up until your chin is above the bar.", video_url = "")
        barbell_deadlift = Workouts(name = "Barbell deadlift", category_id = "Back", description = "a strength training exercise that involves lifting a barbell from the ground to hip level, and then returning it to the ground.", video_url = "")




        db.session.commit()

        print("Seeding complete!")
