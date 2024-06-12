import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";
import "../styles/home.css"

function Home() {
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

  const handleSearch = () => {};
  const handleAddService = () => {};
  const handleRowClick = (id) => () => {
    navigate(`/infoservice`, { state: { id } });
  };

  return (
    <>
      <section className="container">
        <article className="card">
          <div className="search-bar">
            <div className="search">
              <div className="input-wrapper">
                <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/5432f397b9aa45f4a1f1b54a87e9fcf132e23908e329d59ba9ba1ef19388e8fe?apiKey=34896696c8eb4711b53c4cb2e354d605&" alt="" width="16" />
                <input type="text" className="search-input" placeholder="Search..." aria-label="Search" />
              </div>
              <button className="button" onClick={handleSearch}>
                Search
              </button>
            </div>
            <button className="button" onClick={handleAddService}>
              <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/d322eb2c900627c1c0432bf23dfda65d4720f3b4b6381543703e324a72370a2e?apiKey=34896696c8eb4711b53c4cb2e354d605&" alt="Add Service Icon" width="16" />
              <span>Add service</span>
            </button>
          </div>
          <header className="header">
            <div className="header-left">
              <span className="info-title">Plate</span>
              <span className="desc">Description</span>
            </div>
            <div className="header-right">
              <span className="info-title">Start Date</span>
              <span className="info-title">End Date</span>
              <span className="info-title">Start Hour</span>
              <span className="info-title">End Hour</span>
            </div>
          </header>
          <div className="table">
            {events.map((event) => (
              <button className="row" key={event.id} onClick={handleRowClick(event.id)}>
                <div className="row-left">
                  <div className="balance">
                    <span className="amount">{event.vehicle_plate}</span>
                  </div>
                  <div className="balance">
                    <span className="amount">{event.obs}</span>
                  </div>
                </div>
                <div className="row-right">
                  <div className="balance">
                    <span className="amount">{event.start_hour}</span>
                  </div>
                  <div className="balance">
                    <span className="amount">{event.end_date}</span>
                  </div>
                  <div className="balance">
                    <span className="amount">{event.start_hour}</span>
                  </div>
                  <div className="balance">
                    <span className="amount">{event.end_hour}</span>
                  </div>
                </div>
              </button>
            ))}
          </div>
          <footer className="table-footer">
            <div className="pagination">
              <span className="pagination-info">1-10 of 97</span>
              <div className="rows-per-page"></div>
            </div>
            <div className="dropdown">
              <button className="button">
                <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/1e5edb8ca2e340b48d0d0bdf543377799c06a79482a2a42629dd8dd4bd5b9d72?apiKey=34896696c8eb4711b53c4cb2e354d605&" alt="Dropdown Icon" width="24" />
              </button>
            </div>
          </footer>
        </article>
      </section>
    </>
  );
}

export default Home;