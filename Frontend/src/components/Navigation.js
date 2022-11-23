import React from "react";
import { NavLink } from "react-router-dom";


function Navigation() {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            <center><h1>My Portal</h1></center>
          </NavLink>
          <div>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/AddFlight">
                <h1>AddFlight</h1>
                  {/* <span className="sr-only">(current)</span> */}
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/Monitor">
                  <h1>View Scheduled Flights</h1>
                </NavLink>
              </li>
              
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navigation;