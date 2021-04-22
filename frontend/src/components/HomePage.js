import React, { Component } from "react";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/frontend">
            <p>This is the home page for implementing the react app</p>
          </Route>
         
        </Switch>
      </Router>
    );
  }
}
