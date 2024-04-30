import React, {useState} from 'react';

function App(props) {
  const [counter, setCounter] = useState(0);

  const colorStyle = {
    color:props.color,
    fontSize:props.size
  }
  
  let incrementCounter = () => {
    setCounter(counter + 1);
  }

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
    </div>
  );
}

export default App;