import React, { Component } from 'react';

import { Button, Modal } from 'react-bootstrap';


class OrderModal extends Component {
    state = {
        modalSuccess: {
            body: 'Venda cadastrada com sucesso.',
            buttonText: 'Fechar',
        },
        modalError: {
            body: 'Não foi possível realizar a venda.',
            buttonText: 'Tentar Novamente',
        }
    }

    handleClose = () => (this.props.handleClose())

    render() {
        const { show } = this.props;
        const modal = show ? this.state.modalSuccess : this.state.modalError 
        return (
            <Modal show={show} onHide={this.handleClose} centered>
              <Modal.Body>{modal.body}</Modal.Body>
              <Modal.Footer>
                <Button variant="success" onClick={this.handleClose}>
                  {modal.buttonText}
                </Button>
              </Modal.Footer>
            </Modal>
        )
    }
}

export default OrderModal;