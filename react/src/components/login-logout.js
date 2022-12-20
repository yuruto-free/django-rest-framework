import axios from 'axios';
import { useGoogleLogin, googleLogout } from '@react-oauth/google';

const getLoginStatus = (user) => Object.keys(user).length > 0;
const baseURL = 'http://localhost:8000';
const redirectURL = 'http://localhost:3000';

const Login = (props)  => {
  const handleAuthorizationCode = (response) => {
    // Convert authorization code to access token
    axios.post(`${baseURL}/api/login/social/jwt-pair-user/`, {
      provider: 'google-oauth2',
      code: response.code,
      redirect_uri: redirectURL,
    }).then((res) => {
      props.onSuccessCallback(res.data);
    }).catch((err) => {
      console.log('Auth Error:', err);
    });
  };

  const login = useGoogleLogin({
    onSuccess: handleAuthorizationCode,
    onError: (err) => console.log(err),
    flow: 'auth-code',
  });

  if (getLoginStatus(props.user)) {
    return null;
  }

  return (
    <button onClick={() => login()}>
        {props.text}
    </button>
  );
};

const Logout = (props) => {
  const handleLogout = () => {
    googleLogout();
    props.onClick();
  };

  if (!getLoginStatus(props.user)) {
    return null;
  }

  return (
    <div>
      <button onClick={() => handleLogout()}>
        {props.text}
      </button>
    </div>
  );
};

export {
  Login,
  Logout,
};