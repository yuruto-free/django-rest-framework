import { useState } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { Login, Logout } from './components/login-logout.js';
import UserInfo from './components/user-info.js';

function App() {
  const googleClientID = process.env.REACT_APP_GOOGLE_CLIENT_ID;
  const [user, setUser] = useState({});

  const handleSocialLogin = (response) => {
    setUser(response);
  };
  const handleSocialLogout = () => {
    setUser({});
  };

  return (
    <>
      <GoogleOAuthProvider clientId={googleClientID}>
        <Login
          user={user}
          text="Sign in with Google"
          onSuccessCallback={(response) => handleSocialLogin(response)}
        />
        <UserInfo
          user={user}
        />
        <Logout
          user={user}
          text="Sign out"
          onClick={() => handleSocialLogout()}
        />
      </GoogleOAuthProvider>
    </>
  );
}

export default App;
