import React, { Component } from 'react';


class OrderItem extends Component {
    render() {
        const {item, deleteItem} = this.props
        return (
            <React.Fragment >
                <td>{item.name}</td>
                <td>{item.quantity}</td>
                <td>{item.price}</td>
                <td>{item.total}</td>
                <td>
                    <button type="button" className="btn btn-xs btn-danger img-circle" onClick={() => (deleteItem(item.id))}>&#xff38;</button>
                </td>
            </React.Fragment>
        )
    }
}

export default OrderItem;