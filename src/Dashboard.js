
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import Filters from './components/Filters';
import 'bootstrap/dist/css/bootstrap.min.css';

function Dashboard() {
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/data')
      .then(response => {
        setData(response.data);
        setFilteredData(response.data);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const chartData = {
    labels: filteredData.map(item => item.year),
    datasets: [{
      label: 'Intensity',
      data: filteredData.map(item => item.intensity),
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1
    }]
  };

  return (
    <div className="Dashboard">
      <h1>Data Visualization Dashboard</h1>
      <Filters data={data} setFilteredData={setFilteredData} />
      <div className="chart-container">
        <Bar data={chartData} options={{ scales: { y: { beginAtZero: true } } }} />
      </div>
    </div>
  );
}

export default Dashboard;




// // frontend/src/Dashboard.js
// import React, { useEffect, useState } from 'react';
// import axios from 'axios';
// import { Bar } from 'react-chartjs-2';
// import Filters from './components/Filters';
// import 'bootstrap/dist/css/bootstrap.min.css';

// function Dashboard() {
//   const [data, setData] = useState([]);
//   const [filteredData, setFilteredData] = useState([]);

//   useEffect(() => {
//     axios.get('http://localhost:5000/data')
//       .then(response => {
//         setData(response.data);
//         setFilteredData(response.data);
//       })
//       .catch(error => console.error('Error fetching data:', error));
//   }, []);

//   const chartData = {
//     labels: filteredData.map(item => item.year),
//     datasets: [{
//       label: 'Intensity',
//       data: filteredData.map(item => item.intensity),
//       backgroundColor: 'rgba(75, 192, 192, 0.2)',
//       borderColor: 'rgba(75, 192, 192, 1)',
//       borderWidth: 1
//     }]
//   };

//   return (
//     <div className="Dashboard">
//       <h1>Data Visualization Dashboard</h1>
//       <Filters data={data} setFilteredData={setFilteredData} />
//       <div className="chart-container">
//         <Bar data={chartData} options={{ scales: { y: { beginAtZero: true } } }} />
//       </div>
//     </div>
//   );
// }

// export default Dashboard;
