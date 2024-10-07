import React from "react";
import Workouts from "./Components/Workouts";  // Adjust path based on your file structure
import Home from "./Components/Home"; // Adjust path based on your file structure

function App() {
    return (
        <div>
            <h1 id="workout-list">Workout List</h1>
            <Workouts />
            <Home />
            
        </div>
    );
}

export default App;