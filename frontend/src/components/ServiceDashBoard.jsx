import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";
import ProgressBarComponent from "./ProgessBarComponent";
import Table from "react-bootstrap/esm/Table";

function ServiceDashBoard() {
  const [events, setEvents] = useState([]);
  const navigate = useNavigate();
  const serviceStatus = []
  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get("/service/create");
        setEvents(response.data);
      } catch (error) {
        console.error("Failed to fetch events:", error);
      }
      let events = response.data();
      for (i = 0; i < events.length(); i++)
        {
          try {
            const response = api.get(`/service/infoservice/${events.id}`);
            console.log(response.data.length())
          } catch (error) { 
            console.error("Failed to fetch the service: ", error);
          }
        }
    };
    fetchEvents();
  }, []);

  const handleRowClick = (id) => () => {
    navigate(`/infoservice`, { state: { id } });
  };

  return (
    <Table responsive bordered hover variant="light">
      <thead>
        <tr>
          <th>Id</th>
          <th>Plate</th>
          <th>Description</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Start Hour</th>
          <th>end Hour</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {events?.map((event) => (
          <tr key={event.id} onClick={handleRowClick(event.id)}>
            <th scope="row" key={event.id}>
              {event.id}
            </th>
            <td>{event.vehicle_plate}</td>
            <td>{event.obs}</td>
            <td>{event.start_date}</td>
            <td>{event.end_date}</td>
            <td>{event.start_hour}</td>
            <td>{event.end_hour}</td>
            <td>
              <ProgressBarComponent percen={50} />
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
export default ServiceDashBoard;
