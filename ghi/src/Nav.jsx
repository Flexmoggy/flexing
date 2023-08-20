import React, { useState, useEffect } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useAuthContext } from '@galvanize-inc/jwtdown-for-react';
import useToken from '@galvanize-inc/jwtdown-for-react';

function Nav() {
  const [account, setAccount] = useState("");
  const { token } = useAuthContext();
  const { logout } = useToken();
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logout();
      navigate("")
    } catch (error) {
      console.log(error);
    }
  }

  const fetchWithAPI = () => {
    const url = `${process.env.REACT_APP_API_HOST}/token`;
    fetch(url, {
      credentials: "include",
    })
    .then((response) => response.json())
    .then((data) => {
      setAccount(data.account);
    })
    .catch((error) => console.error(error));
  };

  useEffect(() => {
    fetchWithAPI();
  }, []);

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0 flex-wrap">
              <li className="nav-item">
                <NavLink className="nav-link" to="/my_profile">My Profile</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/profiles">Profiles</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/messages">Messages</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/login">Login</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/signup">Signup</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
        <div className="col-md-3 mb-2 mb-md-0">
        </div>
      </header>

      {/* Footer */}
      <footer className="footer bg-dark text-white text-center py-3">
        <div className="container">
          <p>&copy; {new Date().getFullYear()} Your App Name. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default Nav;
