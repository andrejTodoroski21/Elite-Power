// import React, {useEffect, useState} from "react";
// import { useOutletContext } from 'react-router-dom'

// function Workouts(){
//     const [workouts, setWorkouts] = useState([]);

//     useEffect(() => {
//         fetch ("api/workouts")
//         .then(res => res.json())
//         .then(data => {console.log(data)
//             setWorkouts(data)})
//     },[]);

//     return (
//         <div id="workout-grid">
//             <div className="workout-container">
//                 {workouts.map(workout => (
//                     <div key={workout.name}>  {/* Display the workout name */}
//                     <br></br>
//                         {workout.name}
//                     </div>
//                 ))}
//             </div>
//         </div>
//     );
// }
// export default Workouts
import React, {useEffect, useState} from "react";

function Workouts(){
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        fetch("/api/workouts")  // Make sure the endpoint starts with a "/"
        .then(res => res.json())
        .then(data => {
            console.log(data);  // Log data to make sure picture_url is part of it
            setWorkouts(data);
        });
    },[]);

    return (
        <div id="workout-grid">
            <div className="workout-container">
                {workouts.map(workout => (
                    <div key={workout.name}>  {/* Display the workout name */}
                        <h3>{workout.name}</h3>
                        <img src={workout.picture_url} alt={workout.name}  />  {/* Display the image */}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Workouts;

