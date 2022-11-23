import React, { useState } from 'react';
import FlightForm from './AddFlight';
import jsonData from './dummy.json';

function TableData() {
const [flightData, setflightData] = useState(jsonData);

const tableRows = flightData.map((info) => {
	return (
	<tr>
		<td>{info.time}</td>
		<td>{info.flightno}</td>
	</tr>
	);
});

const addRows = (data) => {
	const totalFlights = flightData.length;
	data.id = totalFlights + 1;
	const updatedFlightData = [...flightData];
	updatedFlightData.push(data);
	setflightData(updatedFlightData);
};

return (
	<div>
	<table className="table table-stripped">
		<thead>
		<tr>
			<th>Sr.NO</th>
			<th>time</th>
			<th>Flight#</th>
		</tr>
		</thead>
		<tbody>{tableRows}</tbody>
	</table>
	<FlightForm func={addRows} />
	</div>
);
}

export default TableData;
