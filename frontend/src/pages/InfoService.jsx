import { useState, useEffect } from "react";
import api from "../api";
import { useNavigate, useLocation } from "react-router-dom";
import * as React from "react";

function Info() {
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
      const updateEventOnGoing = (eventId, res) => {
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
      };

      updateEventOnGoing(eventId, res);
    } catch (error) {
      alert(error);
    }
  };

  return (
    <div className="table table-dark">
      <table className="table-bordered table-hover">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Plate</th>
            <th scope="col">Service</th>
            <th scope="col">Technician</th>
            <th scope="col">OnGoing</th>
            <th scope="col">Start Date</th>
            <th scope="col">Finish Date</th>
            <th scope="col">Total time</th>
          </tr>
        </thead>
        <tbody className="table-light">
          {eventsInfo?.map((event) => (
            <tr>
              <th scope="row">{event.id}</th>
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
      </table>
    </div>
  );
}

export default Info;

//   return (
//     <section className="container">
//       <article className="card">
//         <header className="header">
//           <div className="header-left">
//             <span className="info-title">Plate</span>
//             <span className="info-title">Service</span>
//             <span className="info-title">Technician</span>
//             <span className="info-title">OnGoing</span>
//           </div>
//           <div className="header-right">
//             <span className="info-title">Start Date</span>
//             <span className="info-title">Finish Date</span>
//             <span className="info-title">Total time</span>
//           </div>
//         </header>
//         <div className="table">
//           {eventsInfo?.map((event) => (
//             <label className="row">
//               <div className="row-left">
//                 <div className="balance">
//                   <span className="amount">{event.plate}</span>
//                 </div>
//                 <div className="balance">
//                   <span className="amount">{event.service}</span>
//                 </div>
//                 <div className="balance">
//                   <span className="amount">{event.technician}</span>
//                 </div>
//                 <div className="balance">
//                   <select
//                     value={event.onGoing}
//                     onChange={(e) => handleOnGoingChange(e, event.id)}
//                   >
//                     <option value="1">Por começar</option>
//                     <option value="2">A decorrer</option>
//                     <option value="3">Terminado</option>
//                   </select>
//                 </div>
//               </div>
//               <div className="row-right">
//                 <div className="balance">
//                   <span className="amount">{event.startDate}</span>
//                 </div>
//                 <div className="balance">
//                   <span className="amount">{event.finishDate}</span>
//                 </div>
//                 <div className="balance">
//                   <span className="amount">{event.totalTime}</span>
//                 </div>
//               </div>
//             </label>
//           ))}
//         </div>
//       </article>
//     </section>
//   );
// }
