import React from 'react';
import ReactDom from 'react-dom';
import Header from './componenets/header.jsx';

import './scss/common.sass';

class IndexApp extends React.Component {
  render() {
    return (
      <Header/>
    );
  }
}

ReactDom.render(<IndexApp/>, document.getElementById('root'));
