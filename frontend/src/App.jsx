import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Service from './pages/Service';
import InfoService from "./pages/InfoService"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/services" element={<Service />}/>
        <Route path="/infoservice" element={<InfoService />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;