import React, { Component, Fragment } from 'react';
import { render } from "react-dom";

import Header from './layout/Header';
import Dashboard from './orders/Dashbord';

class App extends Component {
    render() {
        return (<Fragment>
            <Header />
            <Dashboard />
        </Fragment>
        )
    }
}

render(<App />, document.getElementById('app'));