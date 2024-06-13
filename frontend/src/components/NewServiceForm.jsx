import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import Row from "react-bootstrap/Row";
import * as formik from "formik";
import * as yup from "yup";

function NewServiceForm() {
  const { Formik } = formik;

  const schema = yup.object().shape({
    plate: yup.string().required(),
    obs: yup.string().required(),
    entry_date: yup.string().required(),
    start_hour: yup.string().required(),
    end_date: yup.string().required(),
    end_hour: yup.string().required(),
  });

  return (
    <Formik
      validationSchema={schema}
      onSubmit={console.log}
      initialValues={{
        plate: "",
        obs: "",
        entry_date: "",
        start_hour: "",
        end_date: "",
        end_hour: "",
      }}
    >
      {({ handleSubmit, handleChange, values, touched, errors }) => (
        <Form noValidate onSubmit={handleSubmit}>
          <Row className="mb-3">
            <Form.Group as={Col} md="4" controlId="validationFormik01">
              <Form.Label>Plate</Form.Label>
              <Form.Control
                type="text"
                name="Plate"
                placeholder="Ex: 00-00-AA"
                value={values.plate}
                onChange={handleChange}
                isValid={touched.plate && !errors.plate}
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} md="4" controlId="validationFormik02">
              <Form.Label>Observações</Form.Label>
              <Form.Control
                type="text"
                name="obs"
                placeholder="Observações"
                value={values.obs}
                onChange={handleChange}
                isValid={touched.obs && !errors.obs}
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} md="4" controlId="validationFormik03">
              <Form.Label>Start Date</Form.Label>
              <Form.Control
                type="date"
                aria-describedby="inputGroupPrepend"
                name="entry_date"
                value={values.entry_date}
                onChange={handleChange}
                isvalid={touched.entry_date && !errors.entry_date}
              />
              <Form.Control.Feedback>Looks good</Form.Control.Feedback>
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} md="6" controlId="validationFormik04">
              <Form.Label>Start hour</Form.Label>
              <Form.Control
                type="time"
                placeholder="Start hour"
                name="start_hour"
                value={values.start_hour}
                onChange={handleChange}
                isvalid={touched.start_hour && !errors.start_hour}
              />
              <Form.Control.Feedback>Looks good</Form.Control.Feedback>
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} md="3" controlId="validationFormik05">
              <Form.Label>End date</Form.Label>
              <Form.Control
                type="date"
                name="end_date"
                value={values.end_date}
                onChange={handleChange}
                isInvalid={touched.end_date && !errors.end_date}
              />
              <Form.Control.Feedback>Looks good</Form.Control.Feedback>
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} md="3" controlId="validationFormik06">
              <Form.Label>End hour</Form.Label>
              <Form.Control
                type="time"
                placeholder="End hour"
                name="zip"
                value={values.end_hour}
                onChange={handleChange}
                isInvalid={touched.end_hour && !errors.end_hour}
              />
              <Form.Control.Feedback>Looks good</Form.Control.Feedback>
            </Form.Group>
          </Row>
        </Form>
      )}
    </Formik>
  );
}

export default NewServiceForm;
