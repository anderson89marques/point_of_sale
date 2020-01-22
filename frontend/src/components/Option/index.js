import React, { Component } from 'react';


class Option extends Component {
    render() {
        const { person } = this.props
        return (
            <React.Fragment>
                <option key={person.id} name={person.name} value={person.id}>{person.name}</option>    
            </React.Fragment>
        )
    }
}

export default Option;