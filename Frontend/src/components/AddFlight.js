import React, { useEffect, useState } from 'react';
import { useHistory, useNavigate } from 'react-router-dom';
import Navigation from './Navigation';


function FlightForm(props) {
	const isAuth = true;
	const navigate = useNavigate();

	const [flightno, setflightno] = useState('');
	const [airline, setAirline] = useState('');
	const [status, setstatus] = useState('');
	const [schedule, setschedule] = useState('');

	useEffect(()=>{

	},[])

	const changeAirline = (event) => {
		setAirline(event.target.value);
	};

	const changeFlightno = (event) => {
		setflightno(event.target.value);
	};
	const changestatus = (event) => {
		setstatus(event.target.value);
	};
	const changeSchedule = (event) => {
		setschedule(event.target.value);
	};

	const transferValue = (event) => {
		event.preventDefault();
		const val = {
			airline,
			flightno,
			status,
			schedule,
		};
		props.func(val);
		clearState();
	};

	const clearState = () => {
		setflightno('');
		setAirline('');
		setstatus('');
		setschedule('');
	};

	const redirectHome = ()=>{
		navigate("/")
	}

	return (

		<div>
			{
				isAuth ? <>
					<Navigation />
					<label>flightno</label>
					<input type="text" value={flightno} onChange={changeFlightno} />
					<label>airline</label>
					<input type="text" value={airline} onChange={changeAirline} />
					<label>status</label>
					<input type="text" value={status} onChange={changestatus} />
					<label>schedule</label>
					<input type="text" value={schedule} onChange={changeSchedule} />
					<button onClick={transferValue}> Click Me</button></> : redirectHome()
			}
		</div>
	);
}

export default FlightForm;
