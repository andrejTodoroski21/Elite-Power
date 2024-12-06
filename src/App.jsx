import React from "react";
import { Outlet } from "react-router-dom";
import Navbar from "./Components/Navbar";

function App() {
    return (
        <div>
            <h1 id="workout-list"></h1>
            <Navbar />
            <Outlet />
            
            
        </div>
    );
}

export default App;