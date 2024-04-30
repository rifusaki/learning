function App(props) {
  const currDate = new Date();

  return (
    <div>
      <h1>Hello, rifu!</h1>
      <h2>The date & time now is {currDate.toLocaleString()}.</h2>
    </div>
  );
}

export default App;