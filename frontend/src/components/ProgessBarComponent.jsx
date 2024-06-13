import ProgressBar from "react-bootstrap/ProgressBar";

function ProgressBarComponent({ percen }) {
  return <ProgressBar animated now={percen} />;
}

export default ProgressBarComponent;
