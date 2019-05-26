import React, {Component} from 'react';
import BaseRouter from './routes';
import {BrowserRouter as Router} from 'react-router-dom'; 
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';
import ArticleList from './containers/ArticalListView';
import {connect} from 'react-redux';
import * as actions from './store/actions/auth'
class App extends Component {
 componentDidMount(){
   this.props.onTryAutoSignup();
 }
  
  render(){
    return (
      <div className = "App">
      <CustomLayout {...this.props}>
      <BaseRouter/>
      </CustomLayout>
      </div>
    )
  }
}

const mapStateToProps = state =>{
  return {
    isauthenticated: state.token != null
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () =>dispatch(actions.authCheckState)
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(App);