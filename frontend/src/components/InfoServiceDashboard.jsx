import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate, useLocation } from "react-router-dom";
import * as React from "react";
import Table from "react-bootstrap/Table";
import Form from "react-bootstrap/Form";

function InfoDashboard() {
  const [eventsInfo, setEvents] = useState([]);
  const location = useLocation();
  const navigate = useNavigate();
  const { id } = location.state || {};

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get(`/service/infoservice/${id}`);
        console.log(response.data);
        setEvents(response.data);
      } catch (error) {
        console.error("Failed to fetch events:", error);
      }
    };
    fetchEvents();
  }, []);

  const handleOnGoingChange = async (e, eventId) => {
    e.preventDefault();
    try {
      const res = await api.put(`/service/infoservice/${eventId}`, {
        onGoing: e.target.value,
      });
      setEvents(
        eventsInfo.map((event) =>
          event.id === eventId
            ? {
                ...event,
                onGoing: res.data.onGoing,
                startDate: res.data.startDate,
                finishDate: res.data.finishDate,
                totalTime: res.data.totalTime,
              }
            : event
        )
      );
    } catch (error) {
      alert(error);
    }
  };

  const handleTechChange = async (e, eventId) => {
    e.preventDefault();
    try {
      const res = await api.put(`/service/infoservice/${eventId}`, {
        technician: e.target.value,
      });
      setEvents(
        eventsInfo.map((event) =>
          event.id === eventId
            ? {
                ...event,
                technician: res.data.idTechnician.name,
              }
            : event
        )
      );
    } catch (error) {
      alert(error);
    }
  };

  const get_formattedDate = (dateString) => {
    if (!dateString || isNaN(new Date(dateString).getTime())) {
      return "N/A";
    }
    const date = new Date(dateString);
    const options = {
      hour: "2-digit",
      minute: "2-digit",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour12: false,
    };
    return new Intl.DateTimeFormat("en-US", options).format(date);
  };

  const get_formattedTime = (timeString) => {
    if (!timeString) {
      return "N/A";
    }
    const parts = timeString.split(":");
    if (parts.length < 3) {
      return "Invalid Time";
    }
    const hours = parts[0];
    const minutes = parts[1];
    const seconds = parts[2].split(".")[0];

    return `${hours}:${minutes}:${seconds}`;
  };

  return (
    <Table responsive bordered variant="light">
      <thead>
        <tr>
          <th>Id</th>
          <th>Plate</th>
          <th>Service</th>
          <th>Technician</th>
          <th>OnGoing</th>
          <th>Start Date</th>
          <th>Finish Date</th>
          <th>Total time</th>
        </tr>
      </thead>
      <tbody>
        {eventsInfo?.map((event) => (
          <tr key={event.id}>
            <th scope="row">{event.id}</th>
            <td>{event.plate}</td>
            <td>{event.service}</td>
            <td>
              <Form.Select
                value={event.technician}
                onChange={(e) => handleTechChange(e, event.id)}
              >
                {event.technicians.map((tech) => (
                  <option key={tech.id}>{tech.name}</option>
                ))}
              </Form.Select>
            </td>
            <td>
              <Form.Select
                value={event.onGoing}
                onChange={(e) => handleOnGoingChange(e, event.id)}
              >
                <option value="1">Por começar</option>
                <option value="2">A decorrer</option>
                <option value="3">Terminado</option>
              </Form.Select>
            </td>
            <td>{get_formattedDate(event.startDate)}</td>
            <td>{get_formattedDate(event.finishDate)}</td>
            <td>{get_formattedTime(event.totalTime)}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}

export default InfoDashboard;
