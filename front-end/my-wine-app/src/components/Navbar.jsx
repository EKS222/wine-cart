import React, { useState } from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom

function Navbar() {
  const [menuActive, setMenuActive] = useState(false);

  const toggleMenu = () => {
    setMenuActive(!menuActive);
  };

  return (
    <div>
      {/* Toggle button for the mobile menu */}
      <div className="menu-toggle" onClick={toggleMenu}>
        <i className={`fa ${menuActive ? 'fa-times' : 'fa-bars'}`} aria-hidden="true"></i>
      </div>

      {/* Mobile menu */}
      <div id="menu" className={`text-left ${menuActive ? 'active' : ''}`}>
        {/* Logo */}
        <div className="logo">
          <img src="../images/logo.png" alt="Logo" />
        </div>
        {/* Menu items */}
        <ul className="offcanvas_main_menu_horizontal">
          <li className="menu-item-has-children active">
            {/* Use Link component with 'to' prop for routing */}
            <Link to="/">Home</Link>
          </li>
          <li>
            {/* Use Link component with 'to' prop for routing */}
            <Link to="/wines">Shop Wines</Link>
          </li>
          <li className="menu-item-has-children">
            {/* Use Link component with 'to' prop for routing */}
            <Link to="/about">About Us</Link>
          </li>
          <li className="menu-item-has-children">
            {/* Use Link component with 'to' prop for routing */}
            <Link to="/reviews">Reviews Page</Link>
          </li>
        </ul>

        {/* User link */}
        <ul className="menu-item-children">
          {/* Use Link component with 'to' prop for routing */}
          <Link to="/login" className="login-link">
            <i className="fa fa-user-o" aria-hidden="true"></i> User
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;