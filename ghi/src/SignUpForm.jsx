import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react"; // Assuming the correct import from the library

function SignUpForm() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const { login } = useAuthContext(); // Adjusted to useAuthContext
    const navigate = useNavigate();

    const handleFirstNameChange = (e) => {
        setFirstName(e.target.value);
    }

    const handleLastNameChange = (e) => {
        setLastName(e.target.value);
    }

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    }

    const handleUserNameChange = (e) => {
        setUserName(e.target.value);
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
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

        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(accountData),
            headers: {
                "Content-Type": "application/json"
            }
        };

        try {
            const response = await fetch(PostUrl, fetchConfig);
            if (response.ok) {
                await login(userName, password);
                setFirstName('');
                setLastName('');
                setEmail('');
                setUserName('');
                setPassword('');
                navigate('/');
            } else {
                console.error("Error creating account");
            }
        } catch (error) {
            console.error("Error creating account: ", error);
        }
    }

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div style={{ backgroundColor: "white", color: "#662d91" }} className="shadow p-4 mt-4 rounded-3">
                    <h1 className="mb-3">Sign Up</h1>
                    <form onSubmit={handleSubmit} id="create-account-form">
                        {/* ... (input fields) ... */}
                        <button type="submit" className="btn btn-primary">Sign Up</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default SignUpForm;
