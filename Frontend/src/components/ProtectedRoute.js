import React from "react";
import { Redirect, Route } from "react-router-dom";
import Home from "./Home";

function ProtectedRoute({ component: Component, ...restOfProps }) {
  const isAuthenticated = localStorage.getItem("isAuthenticated");
  console.log("this", isAuthenticated);

  return (
    <Route
      {...restOfProps}
      render={(props) =>
        isAuthenticated ? <Component {...props} /> : <Home/>
      }
    />
  );
}

export default ProtectedRoute;