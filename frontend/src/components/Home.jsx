import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";
import "../styles/homeStyle.css"

// function Home({route}) {
//     const [events, setEvents] = useState([]);
  
//     useEffect(() => {
//       // Fetch events from the API
//       const fetchEvents = async () => {
//         try {
//           const response = await api.get(route);
//           console.log(response.data);
//           setEvents(response.data);
//         } catch (error) {
//           console.error("Failed to fetch events:", error);
//         }
//       };
  
//       fetchEvents();
//     }, []); // Empty dependency array means this effect runs once on mount
  
//     return (
//       <div>
//         <h2>Event Dashboard</h2>
//         <table>
//           <thead>
//             <tr>
//               <th>ID</th>
//               <th>Vehicle Plate</th>
//               <th>Entry Date</th>
//               <th>Start Hour</th>
//               <th>End Date</th>
//               <th>End Hour</th>
//             </tr>
//           </thead>
//           <tbody>
//             {events.map((event) => (
//               <tr key={event.id}>
//                 <td>{event.id}</td>
//                 <td>{event.vehicle_plate}</td>
//                 <td>{event.entry_date}</td>
//                 <td>{event.start_hour}</td>
//                 <td>{event.end_date}</td>
//                 <td>{event.end_hour}</td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//       </div>
//     );
//   }
  
//   export default Home;


function HomePage() {
  const customers = [
    {
      id: 1,
      name: "Ann Culhane",
      status: "Open",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "-$270.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 2,
      name: "Ahmad Rosser",
      status: "Paid",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "$270.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 3,
      name: "Zain Calzoni",
      status: "Open",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "-$20.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 4,
      name: "Leo Stanton",
      status: "Inactive",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "$600.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 5,
      name: "Kaiya Vetrovs",
      status: "Open",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "-$350.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 6,
      name: "Ryan Westervelt",
      status: "Paid",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "-$270.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 7,
      name: "Corey Stanton",
      status: "Due",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "$30.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 8,
      name: "Adison Aminoff",
      status: "Open",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "-$270.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
    {
      id: 9,
      name: "Alfredo Aminoff",
      status: "Inactive",
      desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla...",
      balance: "$70.00",
      balanceCurrency: "CAD",
      balanceChange: "$460.00",
      changeCurrency: "CAD",
      total: "$500.00",
      totalCurrency: "CAD",
    },
  ];

  const handleSearch = () => {};
  const handleAddService = () => {};
  const handleRowClick = (id) => () => {};

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
              <div className="checkbox"></div>
              <span className="status">Status</span>
              <span className="info-title">Plate</span>
              <span className="desc">Description</span>
            </div>
            <div className="header-right">
              <span className="info-title">Start Date</span>
              <span className="info-title">End Date</span>
              <span className="info-title">Total Time</span>
            </div>
          </header>
          <div className="table">
            {customers.map((customer) => (
              <button className="row" key={customer.id} onClick={handleRowClick(customer.id)}>
                <div className="row-left">
                  <div className="checkbox"></div>
                  <span className="status">{customer.status}</span>
                  <span className="desc">{customer.desc}</span>
                </div>
                <div className="row-right">
                  <div className="balance">
                    <span className="amount">{customer.balance}</span>
                    <span className="price">{customer.balanceCurrency}</span>
                  </div>
                  <div className="balance-change">
                    <span className={customer.balanceChange.startsWith("-") ? "change" : "amount"}>
                      {customer.balanceChange}
                    </span>
                    <span className="price">{customer.changeCurrency}</span>
                  </div>
                  <div className="total-amount">
                    <span className="amount">{customer.total}</span>
                    <span className="total-price">{customer.totalCurrency}</span>
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

export default HomePage;