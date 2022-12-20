const UserInfo = (props) => {
  if (Object.keys(props.user).length === 0) {
    return null;
  }

  return (
    <>
      <ul>
      {Object.keys(props.user).map((key) => (
          <li key={key}>{key}: {props.user[key]}</li>
      ))}
      </ul>
    </>
  );
};

export default UserInfo;