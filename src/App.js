import React, { Component } from 'react';
import './App.css';
import data from './tidied.json'
import BarChart from 'react-bar-chart'

const margin = {top: 20, right: 20, bottom: 200, left: 100};

class App extends Component {
  render() {
    return (
      <div className="app">
        <header className="app-header">
          <h1 className="app-title">reactji-tally</h1>
        </header>
        <BarChart
          ylabel='Frequency'
          width={800}
          height={600}
          data={data}
          margin={margin} />
      </div>
    );
  }
}

export default App;
