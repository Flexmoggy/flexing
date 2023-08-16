import React from 'react';
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './index.css';
import ContextProvider from './ContextStore.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ContextProvider>
      <AuthProvider>
        <App />
      </AuthProvider>
    </ContextProvider>
  </React.StrictMode>
);
