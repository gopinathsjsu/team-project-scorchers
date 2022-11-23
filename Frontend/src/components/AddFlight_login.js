import  axios from 'axios';
import React,{useState} from 'react' 
import { useNavigate } from 'react-router-dom';
import { BASE_URL } from '../config';

function Login() { 
let history = useNavigate();
	const [isAuth, setIsAuth] = useState(false);
	const [username,setusername]=useState(""); 
	const [passw,setPassw]=useState(""); 
	const[dataInput, setDataInput]=useState("");

	const submitThis=()=>{
		const info={username:username,passw:passw}; 
		setDataInput([info]);
		axios.post(BASE_URL+"/airline_login",info)
				.then((res)=>{
					console.log(res.data);
					setIsAuth(true);
					//redirect to home page
				})
				.catch((err)=>{
					console.log(err);
					//redirect to same page - errors
				})
		
	}
	return(
	<div>
		<form action="" onSubmit={submitThis}> 
			<div> 
			<center><label htmlFor="username">UserName - </label>
				<input type="text" name="username" id="username" value={username} onChange={(e)=>setusername(e.target.value)}/></center>
			</div> 
			<div> 
				<center><label htmlFor="passw">Password  -</label>
			<input type="text" name="passw" id="passw" value={passw} onChange={(e)=>setPassw(e.target.value)}/> </center>
			</div>  
			<center><button type="submit" onClick={() => { history.push("/profile")}}> Login </button></center>
		</form>
	</div>
)}

export default Login