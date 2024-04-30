import axios from 'axios';
import React, {useState, useEffect} from "react";

function App(props) {
  // State for counter
  const [counter, setCounter] = useState(0);
  let incrementCounter = () => {
    setCounter(counter + 1);
  }

  // Color style
  const colorStyle = {
    color:props.color,
    fontSize:props.size
  }

  // Define the state for API data
  const [breeds, setBreeds] = useState([]);
  // Fetching data from API on component mount
  useEffect(() => {
      const url = "https://dogapi.dog/api/v2/breeds";
      axios.get(url)
          .then(response => {
              // Set the fetched data to state
              setBreeds(response.data.data);
          })
          .catch(error => {
              console.error('Error fetching data:', error.message);
          });
  }, []);


  const tableCellStyle = {
    border: '1px solid black'
};

  // Render the component
  return (
    <div>
      <div style={colorStyle}>
        Hello World!
      </div>
      <br/> <br/>
      <div>
        <button onClick={incrementCounter}>Increment</button>
        <br/><br/>
        <div style={{ fontSize: '25px' }}>Counter: {counter}</div>
      </div>

      <br/><br/>

      <div>
            <h2>Table of Dog Breeds</h2>
            <table style={{borderCollapse: 'collapse', width: '70%', border: '2px solid black'}}>
                <thead>
                    <tr>
                        <th style={tableCellStyle}>Name</th>
                        <th style={tableCellStyle}>Life Span (years)</th>
                        <th style={tableCellStyle}>Male Weight (kg)</th>
                        <th style={tableCellStyle}>Female weight (kg)</th>
                        <th style={tableCellStyle}>Hypoallergenic</th>
                    </tr>
                </thead>
                <tbody>
                  {breeds.map((breed, index) => (
                      <tr key={index}>
                          <td style={tableCellStyle}>{breed.attributes.name}</td>
                          <td style={tableCellStyle}>{breed.attributes.life.min} - {breed.attributes.life.max}</td>
                          <td style={tableCellStyle}>{breed.attributes.male_weight.min} - {breed.attributes.male_weight.max}</td>
                          <td style={tableCellStyle}>{breed.attributes.female_weight.min} - {breed.attributes.female_weight.max}</td>
                          <td style={tableCellStyle}>{breed.attributes.hypoallergenic ? 'Yes' : 'No'}</td>
                      </tr>
                  ))}
                </tbody>
            </table>
      </div>
      
      <br/><br/>

      <div>
            <h2>List of Dog Breeds</h2>
            <ul>
                {breeds.map((breed, index) => (
                    <li key={index}>
                        <h3>{breed.attributes.name}</h3>
                        <p>Life Span: {breed.attributes.life.min} - {breed.attributes.life.max} years</p>
                        <p>Male Weight: {breed.attributes.male_weight.min} - {breed.attributes.male_weight.max} kg</p>
                        <p>Female Weight: {breed.attributes.female_weight.min} - {breed.attributes.female_weight.max} kg</p>
                        <p>Hypoallergenic: {breed.attributes.hypoallergenic ? 'Yes' : 'No'}</p>
                    </li>
                ))}
            </ul>
      </div>
    </div>
  );
}

export default App;