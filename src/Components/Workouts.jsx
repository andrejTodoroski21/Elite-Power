import React, {useEffect, useState} from "react";
import { useOutletContext } from 'react-router-dom'

function Workouts(){
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        fetch ("api/workouts")
        .then(res => res.json())
        .then(data => {console.log(data)
            setWorkouts(data)})
    },[]);

    return (
        <div>
            <div className="workout-container">
                {workouts.map(workout => (
                    <div key={workout.name}>  {/* Display the workout name */}
                        {workout.name}
                    </div>
                ))}
            </div>
        </div>
    );
}
export default Workouts

