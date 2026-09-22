import './App.css'

function App() {

  let counter = 35
  const addValue = () => {
    counter = counter + 1
  }
  return (
    <>
      <h1>Chai aur React</h1>
      <h2>Counter value: {counter} </h2>

      <button
      onClick={addValue}
      >Add value</button> <br />
      <button>remove value</button>
    </>
  )
}

export default App