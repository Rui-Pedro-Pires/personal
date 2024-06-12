import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Clientes from './pages/clientesPages';
import HomePage from './pages/Home';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Clientes />}/>
        <Route path="/home" element={<HomePage />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;