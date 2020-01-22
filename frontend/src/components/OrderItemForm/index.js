import React, { Component } from 'react';
import { Col, Form, Button } from 'react-bootstrap';

import api from '../../services/api';


class OrderItemForm extends Component {
    state = {
        description: '',
        quantity: 1
    }

    updateDescrition = (e) => {
        this.setState({
            description: e.target.value
        });
    }

    updateQuantity = (e) => {
        this.setState({
            quantity: e.target.value
        });
    }

    addNewItem = async (e) => {
        e.preventDefault();
        if (this.state.description === '') {
            alert("É preciso buscar por um produto!");
            return;
        }
        
        const response = await api.get(`/products/?search=${this.state.description}`) 
        const results = response.data.results
        if (results.length > 0 ) {
            const { id, name, price } = results[0]
            const item = {
                id: id,
                name: name,
                price: price,
                quantity: this.state.quantity
            }
            this.setState({ description: '', quantity: 1 });
            this.props.addNewItem(item);
        } else {
            alert("Produto não encontrado!");
        }
        
    }
    
    render() {
        return (
            <section>
                <h3>Produtos</h3>
                <Form>
                    <Form.Row>
                        <Col>
                            <Form.Control 
                                placeholder="Busca por código de barras ou descrição" 
                                value={this.state.description}
                                onChange={this.updateDescrition}/>
                        </Col>
                        <Col>
                            <Form.Control 
                                type='number' 
                                placeholder="Quantidade" 
                                value={this.state.quantity}
                                onChange={this.updateQuantity}/>
                        </Col>
                        <Col>
                            <Button type="submit" onClick={this.addNewItem}>Adicionar</Button>
                        </Col>
                    </Form.Row>
                </Form>
            </section>
            
        )
    }
}

export default OrderItemForm;