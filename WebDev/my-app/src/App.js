import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class App extends Component {
  mathTest () {
  	return 3 + 4;
  }

  render() {
    return (
    	<div>	  
      		<h1>Hello world</h1>
      		<h1>{this.mathTest}</h1>
      	</div>
    );
  }
}

export default App;
