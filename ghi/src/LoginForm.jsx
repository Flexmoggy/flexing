import React, { useState } from 'react';
import useToken from '@galvanize-inc/jwtdown-for-react';
import { useNavigate } from 'react-router-dom';

const LoginForm = () => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { login } = useToken();
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
      event.preventDefault();
      try {
        // const url = `${process.env.REACT_APP_API_HOST}/api/token`;
        await login(username, password);
        event.target.reset();
        navigate("/")
      } catch (err) {
        console.error("Error during login: ", err);
      }
  }

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div style={{ backgroundColor: "white", color: "#662d91" }} className="shadow p-4 mt-4 rounded-3">
          <h1 className="mb-3">Login</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-floating mb-3">
              <input style={{ backgroundColor: "white", color: "#662d91" }}
                id="floatingInput"
                type="text"
                className="form-control"
                onChange={(event) => setUsername(event.target.value)}
                placeholder="username"
              />
              <label htmlFor='floatingInput'>Username:</label>
            </div>
            <div className="form-floating mb-3">
              <input style={{ backgroundColor: "white", color: "#662d91" }}
                id="floatingPassword"
                type="password"
                className="form-control"
                onChange={(event) => setPassword(event.target.value)}
                placeholder='Password'
              />
              <label htmlFor='floatingPassword'>Password:</label>
            </div>
            <div>
              <button type="submit" className="btn btn-primary" >Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
