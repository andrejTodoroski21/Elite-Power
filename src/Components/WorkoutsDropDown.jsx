import React, { useState, useEffect } from "react";

function WorkoutsDropdown() {
  const [categories, setCategories] = useState([]);
  const [workouts, setWorkouts] = useState([]);

  // Fetch all categories when the component mounts
  useEffect(() => {
    fetch("/api/categories")
      .then((response) => response.json())
      .then((data) => setCategories(data));
  }, []);

  // Fetch workouts by category when a category is selected
  const handleCategoryClick = (categoryId) => {
    fetch(`/api/workouts/category/${categoryId}`)
      .then((response) => response.json())
      .then((data) => setWorkouts(data));
  };

  return (
    <li className="dropdown">
      <span className="dropdown-title">Workouts</span>
      <ul className="dropdown-menu">
        {categories.map((category) => (
          <li key={category.id}>
            <button
              onClick={() => handleCategoryClick(category.id)}
              className="dropdown-item"
            >
              {category.name}
            </button>
          </li>
        ))}
      </ul>
      <div className="workout-list">
        {workouts.map((workout) => (
          <div key={workout.id} className="workout-item">
            <h3>{workout.name}</h3>
            <p>{workout.description}</p>
            <a href={workout.videourl} target="_blank" rel="noopener noreferrer">
              Watch Video
            </a>
            {workout.picture_url && (
              <img src={workout.picture_url} alt={workout.name} />
            )}
          </div>
        ))}
      </div>
    </li>
  );
}

export default WorkoutsDropdown;
