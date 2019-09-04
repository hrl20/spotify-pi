import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Dashboard from './songs/Dashboard';
import Header from './layout/Header';


class App extends Component {
	render() {
		return (
			<Fragment>
				<Header />
				<div className="container">
					<Dashboard />
				</div>
			</Fragment>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'));