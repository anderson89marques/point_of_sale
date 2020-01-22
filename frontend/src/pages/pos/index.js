import React, { Component } from 'react';
import { Container, Col, Row } from 'react-bootstrap';

import OrderItemInfo from '../../components/OrderItemInfo';
import SaleData from '../../components/SaleData';
import OrderModal from '../../components/OrderModal';
import api from '../../services/api';

import './styles.css'


export default class Pos extends Component {
    initialData = () => {
        return {
            itens: [],
            customer_id: null,
            seller_id: null,
            show: false
        }
    }

    state = this.initialData()

    handleClose = () => {this.setState({show: false});} 
    handleShow = () => {this.setState({show: true});}

    deleteItem = orderId => {
        const itens = this.state.itens.filter((item) => {
            return item.id !== orderId
        });
        this.setState({ itens });
    }

    addNewItem = orderItem => {
        if (orderItem) {
            const itens = [...this.state.itens]
            itens.push(
                {
                    id: orderItem.id,
                    name: orderItem.name,
                    price: orderItem.price,
                    quantity: orderItem.quantity,
                    total: orderItem.price * orderItem.quantity  
                }
            )
            this.setState({ itens })
        } else {
            console.log("Please add a quantity and description value.")
        }
    }

    updateCustomer = (customer_id) => {
        this.setState({ customer_id });
    }

    updateSeller = (seller_id) => {
        this.setState({ seller_id });
    }

    clear = () => {
        this.setState({ ...this.initialData() });
    }

    getSum = (total, num) => {
        return total + Math.round(num);
    }

    sum = (prices) => {
        return prices.reduce(this.getSum, 0);
    }

    sendOrder = async () => {
        if (this.state.itens.length === 0) {
            alert("É preciso selecionar ao menos 1 item.");
            return;
        }

        const { customer_id, seller_id, itens } = this.state;
        const totalPrice = this.sum(itens.map(item => (item.total)))
        const itensToSent = itens.map(item => ( {
            id: item.id,
            quantity: item.quantity,
            price: item.total
        }))
        const data = {
            customer_id: customer_id,
            seller_id: seller_id,
            total_price: totalPrice,
            itens: itensToSent
        }
        const response = await api.post('/orders/', data);
        if (response.status === 201) {
            this.clear();
            this.setState({show: true});
        } else {
            alert("");
        }
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col sm={8}><OrderItemInfo 
                                    orderItens={this.state.itens}  
                                    addNewItem={this.addNewItem}
                                    deleteItem={this.deleteItem}/></Col>
                    <Col sm={4}><SaleData 
                                    orderItens={this.state.itens}
                                    updateCustomer={this.updateCustomer}
                                    updateSeller={this.updateSeller}
                                    clear={this.clear}
                                    sendOrder={this.sendOrder}/></Col>
                </Row>
                <section>
                    <OrderModal show={this.state.show} handleClose={this.handleClose}/>
                </section>
            </Container>
        )
    }
}