import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./App.css";
import Nav from './Nav';
import Me from './Me';
import Profiles from './Profiles';
import ViewProfile from './ViewProfile';
import Messages from './Messages';

function App() {
    return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
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
