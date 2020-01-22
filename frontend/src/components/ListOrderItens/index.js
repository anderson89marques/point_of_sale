import React, { Component } from 'react';
import { Table } from 'react-bootstrap';

import OrderItem from '../../components/OrderItem';


class ListOrderItens extends Component {
    deleteItem = (orderId) => {
        this.props.deleteItem(orderId);
    }

    render() {
        const { orderItens } = this.props; 
        return (
            <Table striped className='itens-table'>
                <thead>
                    <tr>
                        <th>Produto/Serviço</th>
                        <th>Quantidade</th>
                        <th>Preço Unitário</th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {orderItens.map(item => (
                        <tr key={item.id}>
                            <OrderItem item={item} deleteItem={this.deleteItem}/>
                        </tr>
                    ))}   
                </tbody>
            </Table>
        )
    }
}

export default ListOrderItens;