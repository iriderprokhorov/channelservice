import React, { Component } from 'react';
import OrdersService from './OrderService';

const ordersService = new OrdersService();

class Dashboard extends Component {

    constructor() {
        super();
        this.state = {
            orders: []
        };
    }

    componentDidMount() {
        var self = this;
        ordersService.getOrders().then(function (result) {
            console.log(result);
            self.setState({ orders: result })
        });
    }

    render() {
        return (
            <table class="table">
                <thead key="thead">
                    <tr>
                        <th>nNumber</th>
                        <th>Order_number</th>
                        <th>Price_usd</th>
                        <th>Srok_postavki</th>
                        <th>price_rub</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.orders?.map(c =>
                        <tr key={c.pk}>
                            <td>{c.number}</td>
                            <td>{c.order_number}</td>
                            <td>{c.price_usd}</td>
                            <td>{c.srok_postavki}</td>
                            <td>{c.price_rub}</td>
                        </tr>)}
                </tbody>
            </table>
        );
    }
}
export default Dashboard;

