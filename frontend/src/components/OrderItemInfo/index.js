import React, { Component } from 'react';
import OrderItemForm from '../../components/OrderItemForm';
import ListOrderItens from '../../components/ListOrderItens';


class OrderItemInfo extends Component {
    render() {
        return (
            <section>
                <OrderItemForm addNewItem={this.props.addNewItem}/>
                <ListOrderItens orderItens={this.props.orderItens} deleteItem={this.props.deleteItem}/>
            </section>
        )
    }
}

export default OrderItemInfo;