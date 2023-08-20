import React from 'react';
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './index.css';
import ContextProvider from './ContextStore.jsx';

function Main() {
  const { token } = useAuthContext();

  return (
    <div className="px-4 py-5 my-5 text-center">
      <h1 className="display-5 fw-bold text-body">Game Night</h1>
      <div className="col-lg-6 mx-auto">
        <p className="lead mb-4">Welcome to Game Night, a newly built app that allows users to create and host game nights with their friends and family. Sign up to discover more awesome features of our app!</p>
      </div>
    </div>
  );
}
export default Main;

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ContextProvider>
      <AuthProvider>
        <App />
        <Main />
      </AuthProvider>
    </ContextProvider>
  </React.StrictMode>
);
