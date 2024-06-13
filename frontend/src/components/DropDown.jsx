import Dropdown from "react-bootstrap/Dropdown";

function DropDown({children}) {
  return (
    <>
      <Dropdown data-bs-theme="dark">
        <Dropdown.Toggle id="dropdown-button-dark-example1" variant="secondary">
          {children}
        </Dropdown.Toggle>
        <Dropdown.Menu>
          <Dropdown.Item>Por começar</Dropdown.Item>
          <Dropdown.Item>A decorrer</Dropdown.Item>
          <Dropdown.Item>Terminado</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </>
  );
}

export default DropDown;
