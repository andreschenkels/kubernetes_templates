import React, { Component } from 'react';

const API_URL = process.env.API_URL;

class HelloWorld extends Component {
  constructor(props) {
    super(props);

    this.state = {
      message: null,
    };
  }

  componentDidMount() {
    fetch(API_URL + '/')
      .then(response => response.json())
      .then(data => this.setState({ message: data }));
  }
  render() {
    return (
      <div className="hello-world">
        <h1>{this.state.message}</h1>
      </div>
    );
  }
}

export default HelloWorld;
