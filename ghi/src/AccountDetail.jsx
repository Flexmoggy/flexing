import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";

function AccountDetails(props) {
    const { token } = useAuthContext();
    const [account, setAccount] = useState(null);
    const { id } = useParams();

    const fetchAccount = async () => {
        try {
            const url = `${process.env.REACT_APP_API_HOST}/api/accounts/${id}`;
            const response = await fetch(url, {
                headers: {
                    Authorization: `Bearer ${token}`
                },
            });
            if (response.ok) {
                const fetchedAccount = await response.json();
                setAccount(fetchedAccount);
            } else {
                console.error("Error fetching account details");
            }
        } catch (error) {
            console.error("Error fetching account details:", error);
        }
    };

    useEffect(() => {
        fetchAccount();
    }, [id, token]); // Add id and token to the dependency array

    return (
        <div className='row'>
            <div className='offset-3 col-6'>
                <div style={{ backgroundColor: "white", color: "#662d91" }} className='shadow p-4 mt-4 rounded-3'>
                    <h1>Account Details</h1>
                    {account ? (
                        <>
                            <div>Name: {account.first_name} {account.last_name}</div>
                            <div>Username: {account.user_name}</div>
                        </>
                    ) : (
                        <div>Loading account details...</div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default AccountDetails;
