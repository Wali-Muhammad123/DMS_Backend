import { Box, Typography } from '@chakra-ui/react';
const HeaderNav = () => {
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container-fluid">
        <a className="navbar-brand">BMS</a>
        <form className="d-flex">
          <button className="btn btn-outline-success" type="submit">
            Donate
          </button>
        </form>
      </div>
    </nav>
  );
};

export default HeaderNav;
