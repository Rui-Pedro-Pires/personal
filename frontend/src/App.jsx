import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Clientes from './pages/clientesPages';
import HomePage from './pages/Home';
import Info from "./pages/InfoService"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Clientes />}/>
        <Route path="/home" element={<HomePage />}/>
        <Route path="/infoservice" element={<Info />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;