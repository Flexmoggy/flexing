import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useToken from "@galvanize-inc/jwtdown-for-react";

function SignUpForm() {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    // const { register } = useToken();
    const { login } = useToken();
    const navigate = useNavigate();

    const handleFirstNameChange = (e) => {
        const value = e.target.value;
        setFirstName(value);
    }

    const handleLastNameChange = (e) => {
        const value = e.target.value;
        setLastName(value);
    }

    const handleEmailChange = (e) => {
        const value = e.target.value;
        setEmail(value);
    }

    const handleUserNameChange = (e) => {
        const value = e.target.value;
        setUserName(value);
    }

    const handlePasswordChange = (e) => {
        const value = e.target.value;
        setPassword(value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const PostUrl = `${process.env.REACT_APP_API_HOST}/api/accounts`;

        const accountData = {
            first_name: firstName,
            last_name: lastName,
            email: email,
            user_name: userName,
            password: password,
        };
        console.log(accountData)
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(accountData),
            headers: {
                "Content-Type": "application/json"
            }
        }
        const response = await fetch(PostUrl, fetchConfig);
        if (response.ok) {
            await login(userName, password);
            e.target.reset();
            navigate('/')
        }
    }

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div style={{ backgroundColor: "white", color: "#662d91" }} className="shadow p-4 mt-4 rounded-3">
                    <h1 className="mb-3">Sign Up</h1>
                    <form onSubmit={(e) => handleSubmit(e)} id="create-account-form">
                        <div className="form-floating mb-3">
                            <input value={firstName} onChange={handleFirstNameChange} placeholder="first name" required type="text" name="first_name" id="first_name" className="form-control"/>
                            <label htmlFor="first_name">First Name:</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input value={lastName} onChange={handleLastNameChange} placeholder="last name" required type="text" name="last_name" id="last_name" className="form-control"/>
                            <label htmlFor="last_name">Last Name:</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input value={email} onChange={handleEmailChange} placeholder="email" required type="text" name="email" id="email" className="form-control"/>
                            <label htmlFor="email">Email:</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input value={userName} onChange={handleUserNameChange} placeholder="user_name" required type="text" name="user_name" id="user_name" className="form-control"/>
                            <label htmlFor="user_name">Username:</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input value={password} onChange={handlePasswordChange} placeholder="password" required type="password" name="password" id="password" className="form-control"/>
                            <label htmlFor="password">Password:</label>
                        </div>
                        <button className="btn btn-primary">Sign Up</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SignUpForm;
