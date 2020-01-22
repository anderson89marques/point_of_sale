import React, { Component } from 'react';
import { Col, Row, Form, Button } from 'react-bootstrap';

import Option from '../../components/Option';

import api from '../../services/api';


class SaleData extends Component {
    state = {
        customers: [],
        sellers: [],
        customer_id: null
    }
    
    componentDidMount() {
        this.loadCustomers();
        this.loadSellers();
    }

    loadCustomers = async () => {
        const response = await api.get('/customers');
        const customers = response.data.results; 
        this.setState({ customers });
    }

    loadSellers = async () => {
        const response = await api.get('/sellers');
        const sellers = response.data.results; 
        this.setState({ sellers });
    }

    getSum = (total, num) => {
        return total + Math.round(num);
    }

    sum = (prices) => {
        return prices.reduce(this.getSum, 0);
    }

    updateCustomer = (e) => {
        const customer_id = e.target.value;
        this.setState({customer_id});
        this.props.updateCustomer(customer_id);
    }
    
    updateSeller = (e) => {
        const seller_id = e.target.value;
        this.props.updateSeller(seller_id);
    }

    clear = (e) => {
        e.preventDefault();
        this.props.clear();
    }

    sendOrder = (e) => {
        e.preventDefault();
        if (this.state.customer_id == null) {
            alert("É preciso selecionar ao menos o customer.");
            return;
        };
        this.props.sendOrder();
    }

    render () {
        const { customers, sellers } = this.state;
        const { orderItens } = this.props
        return (
            <div>
                <h3>Dados Venda</h3>
                <section className='selection-form'>
                    <Form>
                        <Form.Row>
                            <Form.Label>Selecionar um cliente</Form.Label>
                            <Form.Control as="select" onChange={this.updateCustomer}>
                            <option value={undefined}>SELECIONE CLIENTE</option>
                            {customers.map((customer => 
                                <Option person={customer}/>
                            ))}                    
                            </Form.Control>
                        </Form.Row>
                        <br/>
                        <Form.Row>
                            <Form.Label>Selecionar um vendedor</Form.Label>
                            <Form.Control as="select">
                            <option value={undefined}>SELECIONE VENDEDOR</option>
                            {sellers.map((seller => 
                                <Option person={seller}/>
                            ))}                    
                            </Form.Control>
                        </Form.Row>
                    </Form>
                </section>
                <section className='send-order'>
                <Row>
                    <Col>
                        <p><strong>Valor Total R$:</strong></p>
                    </Col>
                    <Col>
                        <strong>{this.sum(orderItens.map(item => (item.total)))}</strong>
                    </Col>
                </Row>
                <Form>
                    <Form.Row>
                        <Col>
                            <Button type="submit" onClick={this.clear}>Cancelar</Button>
                        </Col>
                        <Col>
                            <Button variant="success" type="submit" onClick={this.sendOrder}>Finalizar</Button>
                        </Col>
                    </Form.Row>
                </Form>
                </section>
            </div>
        )
    }
}

export default SaleData;