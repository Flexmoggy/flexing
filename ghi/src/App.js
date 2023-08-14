import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./App.css";
import Nav from './Nav';
import Construct from './Construct.js';

function App() {
    return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<Construct />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
