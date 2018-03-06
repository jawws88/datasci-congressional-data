import React, { Component } from 'react';
import request from 'superagent';
import { Alert } from 'react-bootstrap/lib';

import safeJSONParse from '../util/safeJSONParse';
import BarChart from './charts/BarChart.jsx';
import mockData from '../mock/data.json';

/**
 * The toplevel application component to render as the root node.
 */
class App extends Component {
    state = {
        error: null,
        data: null,
    }

    /**
     * Get the data from the API endpoint.
     * @param {Function} cb - The callback to call.
     */
    getData = (cb) => {
        request.get('http://localhost:8000/api/models/candidate_contributions/')
        .end((err, res) => {
            if (err) {
                return cb(err);
            }
            const { error, data } = safeJSONParse(res.text);
            if (error) {
                return cb(error);
            }
            cb(null, data);
        });
    }

    /**
     * Check the current state of the component and return the page content.
     */
    getContributions = () => {
        const { error, data } = this.state;
        if (error) {
            return (
                <Alert bsStyle="danger">
                    <h3>Internal Error.</h3>
                    <p>{`${error}`}</p>
                </Alert>
            )
        }
        return data && data.map(contribution => (
            <li key={contribution.transaction_id}>
                {contribution.donor_name}{' $'}
                {contribution.transaction_amount}
            </li>
        ))
    }

    componentWillMount() {
        this.getData((error, data) => this.setState({ error, data }));
    }

    render() {
        return (
            <div>
                <h1>Congressional Data</h1>
                <BarChart data={mockData}
                    width={600}
                    height={450}
                    barColor='steelBlue'
                />
                <div className="contribution-list">
                <p>
                    Below are some candidate contributions loaded from the API
                    server. Now let's visualize them!
                </p>
                    {this.getContributions()}
                </div>
            </div>
        )
    }
}

export default App;
