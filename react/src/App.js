import { useEffect, useState } from 'react';
//import axios from 'axios';
//import jwt_decode from 'jwt-decode';
//import { GoogleLogin, GoogleOAuthProvider  } from '@react-oauth/google';

function App() {
  const [user, setUser] = useState({});
  const baseURL = 'http://localhost:8000';
  const drfClientID = process.env.REACT_APP_DRF_CLIENT_ID;
  const drfClientSecret = process.env.REACT_APP_DRF_CLIENT_SECRET;
  const googleClientID = process.env.REACT_APP_GOOGLE_CLIENT_ID;

  return (
    <div>
    </div>
  );
}

export default App;
