import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
// import './Navbar.css'; // Make sure to include the CSS file for styling

function Home() {
  return (
    <div>

      {/* Your homepage content here */}
      <div className="content">
        <h2>Welcome to MyWebsite!</h2>
        <p>This is the homepage content.</p>
      </div>
    </div>
  );
}

export default Home;
