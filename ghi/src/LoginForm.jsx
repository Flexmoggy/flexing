import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react"; // Assuming the correct import from the library

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { login } = useAuthContext(); // Adjusted to useAuthContext
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await login(username, password);
            setUsername(""); // Clear username after successful login
            setPassword(""); // Clear password after successful login
            navigate("/"); // Navigate to home page after successful login
        } catch (err) {
            console.error("Error during login: ", err);
        }
    };

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div style={{ backgroundColor: "white", color: "#662d91" }} className="shadow p-4 mt-4 rounded-3">
                    <h1 className="mb-3">Login</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="form-floating mb-3">
                            <input
                                id="floatingInput"
                                type="text"
                                className="form-control"
                                value={username} // Controlled input value
                                onChange={(event) => setUsername(event.target.value)}
                                placeholder="username"
                            />
                            <label htmlFor='floatingInput'>Username:</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input
                                id="floatingPassword"
                                type="password"
                                className="form-control"
                                value={password} // Controlled input value
                                onChange={(event) => setPassword(event.target.value)}
                                placeholder='Password'
                            />
                            <label htmlFor='floatingPassword'>Password:</label>
                        </div>
                        <div>
                            <button type="submit" className="btn btn-primary">Login</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default LoginForm;
