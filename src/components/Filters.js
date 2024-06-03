// frontend/src/components/Filters.js
import React, { useState } from 'react';

function Filters({ data, setFilteredData }) {
  const [selectedYear, setSelectedYear] = useState('');
  const [selectedTopic, setSelectedTopic] = useState('');
  const [selectedSector, setSelectedSector] = useState('');
  const [selectedRegion, setSelectedRegion] = useState('');

  const handleFilter = () => {
    let filtered = data;

    if (selectedYear) {
      filtered = filtered.filter(item => item.year === parseInt(selectedYear, 10));
    }

    if (selectedTopic) {
      filtered = filtered.filter(item => item.topic === selectedTopic);
    }

    if (selectedSector) {
      filtered = filtered.filter(item => item.sector === selectedSector);
    }

    if (selectedRegion) {
      filtered = filtered.filter(item => item.region === selectedRegion);
    }

    setFilteredData(filtered);
  };

  return (
    <div className="filters-container">
      <div className="filter">
        <label>Year:</label>
        <input
          type="number"
          value={selectedYear}
          onChange={e => setSelectedYear(e.target.value)}
        />
      </div>
      <div className="filter">
        <label>Topic:</label>
        <input
          type="text"
          value={selectedTopic}
          onChange={e => setSelectedTopic(e.target.value)}
        />
      </div>
      <div className="filter">
        <label>Sector:</label>
        <input
          type="text"
          value={selectedSector}
          onChange={e => setSelectedSector(e.target.value)}
        />
      </div>
      <div className="filter">
        <label>Region:</label>
        <input
          type="text"
          value={selectedRegion}
          onChange={e => setSelectedRegion(e.target.value)}
        />
      </div>
      <button onClick={handleFilter}>Apply Filters</button>
    </div>
  );
}

export default Filters;
