import React, { useEffect } from "react";
import Login from "./AddFlight_login";

function Home() {
  const myStyle={
    backgroundImage: 
"url('https://media.geeksforgeeks.org/wp-content/uploads/rk.png')",
    height:'100vh',
    marginTop:'-70px',
    fontSize:'50px',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
};
  useEffect(()=>{
    console.log("Home page rendered");
  },[])
  return (
    <div style={myStyle}>
      <div className="home">
      <div class="container">
        <div class="row align-items-center my-5">
          <div class="col-lg-7">
            <img
              class="img-fluid rounded mb-4 mb-lg-0"
              src="http://placehold.it/900x400"
              alt=""
            />
          </div>
          <div class="col-lg-5">
          <p style={{fontSize: '2rem'}}> <center><h1 class="font-weight-light">Scorchers <span className="red-text">Avaiation </span> </h1></center></p>
            
            <p>
              <center><h6> <i>Enter your credentials</i> </h6> </center>
              <Login/>
            </p>
          </div>
        </div>
      </div>
    </div> </div>
    
  );
}

export default Home;