import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react"; // Assuming the correct import from the library

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { login } = useAuthContext(); // Adjusted to useAuthContext
    const navigate = useNavigate(); // Renamed redirect to navigate

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await login(username, password);
            event.target.reset();
            navigate('/boardgames/list'); // Updated to use the navigate function
        } catch (err) {
            console.error("Error during login: ", err);
        }
    }

    return (
        <div className="card text-bg-light mb-3">
            <h5 className="card-header">Login</h5>
            <div className="card-body">
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Username:</label>
                        <input
                            name="username"
                            type="text"
                            className="form-control"
                            value={username} // Added value attribute
                            onChange={(event) => setUsername(event.target.value)}
                        />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Password:</label>
                        <input
                            name="password"
                            type="password"
                            className="form-control"
                            value={password} // Added value attribute
                            onChange={(event) => setPassword(event.target.value)}
                        />
                    </div>
                    <div>
                        <button type="submit" className="btn btn-primary">Login</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default LoginForm;
