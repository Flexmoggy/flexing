import { NavLink } from 'react-router-dom';

function Nav() {
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
            </ul>
          </div>
        </div>
      </nav>
    </div>

  )
}

export default Nav;