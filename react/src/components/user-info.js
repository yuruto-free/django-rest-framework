import axios from 'axios';

const UserInfo = (props) => {
  if (Object.keys(props.user).length === 0) {
    return null;
  }

  const handleCollectUserList = (user) => {
    const baseURL = 'http://localhost:8000';
    const token = user.token;

    // Collect user data used by access token
    axios.get(`${baseURL}/api/accounts/users/`, {
      headers: {
        Authorization: `JWT ${token}`,
        'Content-Type': 'application/json; charset=utf-8',
      },
    }).then((res) => {
      const userLists = document.querySelector('#user-lists');
      const out ='<ul>' + res.data.map((_user, idx) => {
        const _tmp = Object.entries(_user).map(([key, value]) => `<li>${key}: ${value}</li>`).join(' ');
        return `<li key=${idx}><ul>${_tmp}</ul></li>`;
      }).join('\n') + '</ul>';
      userLists.innerHTML = out;
    }).catch((err) => {
      console.log('Error:', err);
    });
  };

  return (
    <>
      <ul>
      {Object.keys(props.user).map((key) => (
          <li key={key}>{key}: {props.user[key]}</li>
      ))}
      </ul>
      <h1>User List</h1>
      <div id="user-lists"></div>
      <button onClick={() => handleCollectUserList(props.user)}>
        Collect User List
      </button>
    </>
  );
};

export default UserInfo;