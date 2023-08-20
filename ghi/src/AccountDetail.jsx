import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import useAuthContext from "@galvanize-inc/jwtdown-for-react";

function AccountDetails(props) {
  const { token } = useAuthContext();
  const [account, setAccount] = useState('');
  const { id } = useParams();
  // console.log(id)
  // const navigate = useNavigate();

  const fetchAccount = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/api/accounts/${id}`;
    // console.log(id)
    const response = await fetch(url, {
      headers: {
        Authorization: `Bearer ${token}`
      },
    });
    const fetchedAccount = await response.json();
    setAccount(fetchedAccount);
    // console.log(fetchedAccount)
  }

  useEffect(() => {
    fetchAccount();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className='row'>
      <div className='offset-3 col-6'>
        <div style={{ backgroundColor: "white", color: "#662d91" }} className='shadow p-4 mt-4 rounded-3'>
          <h1>Account Details</h1>
          <div>Name: {account.first_name} {account.last_name}</div>
          <div>Username: {account.user_name}</div>
        </div>
      </div>
    </div>
  );
}

export default AccountDetails;
