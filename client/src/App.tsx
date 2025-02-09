import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

//material UI library. 
// UI tables can be used. packages.json add there.
//work on this branch list-books
//work on client folder
//move everything to proper project folders like components. 
//see if endpoints are properly being called can we console log on browser. in UI show as a list. 
//basic structure. 
//instead of listing then we can pass to material UI and do it there

//ACTION ITEMS
//work on listing items and get it running for now
//make a new branch for myself. 
//run on gitbash terminal
//python run.py for backend
//npm run dev for frontend

//pull request

function App() {
  const [count, setCount] = useState(0);
  const [books, setBooks] = useState([]);
  const baseURL = 'http://localhost:8080';

  const fetchUsers = async() => {
    const response = await fetch(baseURL + '/api/v1/books');
    const data = await response.json();
    setBooks(data.books);
    console.log(data.books);
  };



  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
          {
            books.map((book, index) => (
              <div key={index}>
                <span>{book.name}</span><br/>
              </div>
            )
          )}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
