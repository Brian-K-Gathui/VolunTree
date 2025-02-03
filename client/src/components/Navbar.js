import React, { useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

const Navbar = () => {
  const [imageError, setImageError] = useState(false);

  return (
    <nav className="navbar navbar-expand-lg bg-white box-shadow">
      <div className="container">
        {/* Brand/Logo */}
        <Link className="navbar-brand" to="/">
          {imageError ? (
            <span>VolunTree 🌳</span>
          ) : (
            <img
              src="/logo.png"
              alt="VolunTree Logo"
              width="250"
              className="me-2"
              onError={() => setImageError(true)}
            />
          )}
        </Link>

        {/* Offcanvas Toggler */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasNavbar"
          aria-controls="offcanvasNavbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Offcanvas Content */}
        <div
          className="offcanvas offcanvas-end"
          tabIndex="-1"
          id="offcanvasNavbar"
          aria-labelledby="offcanvasNavbarLabel"
        >
          <div className="offcanvas-header">
            <button
              type="button"
              className="btn-close text-reset"
              data-bs-dismiss="offcanvas"
              aria-label="Close"
            ></button>
          </div>
          <div className="offcanvas-body">
            {/* Main Nav Items */}
            <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/organizations">Organizations</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/volunteers">Volunteers</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/events">Events</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/tasks">Tasks</Link>
              </li>
              {/* Turn the "Login" link into a secondary button */}
              <li className="nav-item">
                <Link className="btn btn-primary me-2" to="/login">
                  Login
                </Link>
              </li>
              {/* Turn the "Sign Up" link into a primary button */}
              <li className="nav-item">
                <Link className="btn btn-secondary" to="/signup">
                  Sign Up
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
