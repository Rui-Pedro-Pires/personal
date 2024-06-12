import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate, useLocation } from "react-router-dom";
import * as React from "react";

function Info() {
    const [eventsInfo, setEvents] = useState([]);
    const location = useLocation();
    const { id } = location.state || {};
    useEffect(() => {
      // Fetch events from the API
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
    }, []); // Empty dependency array means this effect runs once on mount
  
    return (
      <div>
        <h2>Event Dashboard</h2>
        <table>
          <thead>
            <tr>
              <th>idEvent</th>
              <th>idService</th>
              <th>idTechnician</th>
              <th>onGoing</th>
              <th>startDate</th>
              <th>finishDate</th>
              <th>totalTime</th>
            </tr>
          </thead>
          <tbody>
            {eventsInfo.map((event) => (
              <tr key={event.id}>
                <td>{event.idEvent}</td>
                <td>{event.idService}</td>
                <td>{event.idTechnician}</td>
                <td>{event.onGoing}</td>
                <td>{event.startDate}</td>
                <td>{event.finishDate}</td>
                <td>{event.totalTime}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  
  export default Info;