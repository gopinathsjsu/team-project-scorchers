// import React from "react";
import React, { useState, useEffect } from 'react';
import Navigation from './Navigation';
// import TableData from './Components/Form.js';

const colors = ["#0088FE", "#00C49F", "#FFBB28"];
const delay = 2500;

function Monitor() {

    const [index, setIndex] = React.useState(0);
    const timeoutRef = React.useRef(null);
  
    function resetTimeout() {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    }
  
    const myStyle={
      backgroundImage: 
      "url('https://media.geeksforgeeks.org/wp-content/uploads/rk.png')",
      height:'100vh',
      marginTop:'-70px', 
      fontSize:'30px',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
  };
  
    useEffect(()=>{
      //axios call to fetch data from backend.
    },[])
    
    return (
      <div><div className="slideshow">
      <Navigation/>
      <div
        className="slideshowSlider"
        style={{ transform: `translate3d(${-index * 100}%, 0, 0)` }}
      >
        <div><center><h1>MONITOR </h1></center></div>
        
        {colors.map((backgroundColor, index) => (
          <div
            className="slide"
            key={index}
            style={{ backgroundColor }}
          ></div>
        ))}
      </div>
      {/* <div> <TableData /> </div> */}

      <div className="slideshowDots">
        {colors.map((_, idx) => (
          <div
            key={idx}
            className={`slideshowDot${index === idx ? " active" : ""}`}
            onClick={() => {
              setIndex(idx);
            }}
          ></div>
        ))}
      </div>
    </div></div>
      
    );
  }
  
  export default Monitor;