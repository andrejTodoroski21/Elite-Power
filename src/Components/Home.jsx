import React from 'react';
import { Link } from 'react-router-dom';
// import './Navbar.css'; // Make sure to include the CSS file for styling

function Home() {
  return (
    <div>
      <nav className="navbar">
        <div className="logo">
          <h1>MyWebsite</h1> {/* You can replace this with an image or any other logo */}
        </div>
        <ul className="nav-links">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/workouts">Workouts</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>

      {/* Your homepage content here */}
      <div className="content">
        <h2>Welcome to MyWebsite!</h2>
        <p>This is the homepage content.</p>
      </div>
    </div>
  );
}

export default Home;
