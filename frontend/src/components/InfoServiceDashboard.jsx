import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate, useLocation } from "react-router-dom";
import * as React from "react";
import Table from 'react-bootstrap/Table';

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
            <tr>
              <th scope="row" key={event.id}>{event.id}</th>
              <td>{event.plate}</td>
              <td>{event.service}</td>
              <td>{event.technician}</td>
              <td>
                <select
                  value={event.onGoing}
                  onChange={(e) => handleOnGoingChange(e, event.id)}
                >
                  <option value="1">Por começar</option>
                  <option value="2">A decorrer</option>
                  <option value="3">Terminado</option>
                </select>
              </td>
              <td>{event.startDate}</td>
              <td>{event.finishDate}</td>
              <td>{event.totalTime}</td>
            </tr>
          ))}
      </tbody>
    </Table>
  );
}

export default InfoDashboard;