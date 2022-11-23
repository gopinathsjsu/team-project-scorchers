import logo from './logo.svg';
import './App.css';
import Login from './Components/AddFlight_login';
// import Header from './Components/Header';
import React from 'react';
import Monitor from './Components/Monitor';
import { Routes , Route, Router} from 'react-router-dom';
import Navigation from './Components/Navigation';
import Home from './Components/Home';
import FlightForm from './Components/AddFlight';
import ProtectedRoute from './Components/ProtectedRoute';


function App () {
  return (

    <a>
      {/* <Navigation /> */}
      <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path="login" element={<Login />} />
      <Route path="/AddFlight" element={<FlightForm />} />
      <Route path="/Monitor" element={<Monitor />} />
    </Routes>
    {/* <Footer/> */}
    </a>
  )
}



export default App;
