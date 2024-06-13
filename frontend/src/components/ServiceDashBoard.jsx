import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";
import ProgressBarComponent from "./ProgessBarComponent";
import Table from "react-bootstrap/esm/Table";

function ServiceDashBoard() {
  const [events, setEvents] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get("/service/create");
        setEvents(response.data);
      } catch (error) {
        console.error("Failed to fetch events:", error);
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
          <th>Start Hour</th>
          <th>End Date</th>
          <th>End Hour</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {events?.map((event) => (
          <tr key={event.id} onClick={handleRowClick(event.id)}>
            <th scope="row" key={event.id}>
              {event.id}
            </th>
            <td className="text-nowrap">{event.vehicle_plate}</td>
            <td className="col-4">{event.obs}</td>
            <td>{event.entry_date}</td>
            <td>{event.start_hour}</td>
            <td>{event.end_date}</td>
            <td>{event.end_hour}</td>
            <td>
              <ProgressBarComponent percen={event.percent} />
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
export default ServiceDashBoard;
