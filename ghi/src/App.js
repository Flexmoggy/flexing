import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./App.css";
import Nav from './Nav';
import Me from './Me.js';
import Profiles from './Profiles.js';
import ViewProfile from './ViewProfile.js';
import Messages from './Messages.js';

function App() {
    return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<Profiles />} />
          <Route path="/profiles" element={<Profiles />} />
          <Route path="/my_profile" element={<Me />} />
          <Route path="/view_profile" element={<ViewProfile />} />
          <Route path="/messages" element={<Messages />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
