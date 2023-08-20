import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useEffect, useState } from "react";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import SignUpForm from './SignUpForm';
import LoginForm from './LoginForm';
import AccountDetails from './AccountDetail';
import Footer from './Footer';
import "./App.css";
import Nav from './Nav';
import Me from './Me';
import Profiles from './Profiles';
import ViewProfile from './ViewProfile';
import Messages from './Messages';
import UserDataCard from './UserData';
import Main from './main';

function App() {
  const [userData, setUserData] = useState("");

  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, '');

  const fetchWithAPI = () => {
    const url = `${process.env.REACT_APP_API_HOST}/token`;
    fetch(url, {
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => {
        setUserData(data.account);
      })
      .catch((error) => console.error(error));
  };

  useEffect(() => {
    fetchWithAPI();
  }, []);

  return (
    <AuthProvider baseUrl={`${process.env.REACT_APP_API_HOST}`}>
      <BrowserRouter basename={basename}>
        <Nav userData={userData} />
        <div className="container">
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignUpForm />} />
            <Route path="/accounts/:id" element={<AccountDetails userData={userData} />} />
            <Route path="/profiles" element={<Profiles />} />
            <Route path="/my_profile" element={<Me />} />
            <Route path="/view_profile" element={<ViewProfile />} />
            <Route path="/messages" element={<Messages />} />
            <Route path="/userdata" element={<UserDataCard />} /> {/* Added this line */}
          </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
