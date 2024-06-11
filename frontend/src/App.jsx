import { useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Clientes from './pages/clientesPages';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/">
          <Clientes />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;