import React from 'react';
import {Route, BrowserRouter, Switch, useParams} from "react-router-dom";

import './App.css';
import logo from './assets/kue.png';
import Customer from './components/customer';

function App() {
  return (



    <div className="App">
        <BrowserRouter>

        <Switch>
            <Route path="/customer/:username/:order_id" children={<Customer />}/>
        </Switch>

        </BrowserRouter>   
    
      <header className="App-header">
        <img src={logo} alt="logo" />

      </header>
    </div>
  );
}

export default App;
