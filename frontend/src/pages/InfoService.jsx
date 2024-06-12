import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";

function Info({route}) {
    const [events, setEvents] = useState([]);
  
    useEffect(() => {
      // Fetch events from the API
      const fetchEvents = async () => {
        try {
          const response = await api.get(route);
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
              <th>ID</th>
              <th>Vehicle Plate</th>
              <th>Entry Date</th>
              <th>Start Hour</th>
              <th>End Date</th>
              <th>End Hour</th>
            </tr>
          </thead>
          <tbody>
            {events.map((event) => (
              <tr key={event.id}>
                <td>{event.id}</td>
                <td>{event.vehicle_plate}</td>
                <td>{event.entry_date}</td>
                <td>{event.start_hour}</td>
                <td>{event.end_date}</td>
                <td>{event.end_hour}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  
  export default Info;