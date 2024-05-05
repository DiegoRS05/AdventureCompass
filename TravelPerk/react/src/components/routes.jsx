import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Component2 from './component2';
import Component1 from 'Component1';

function Routes() {
  return (
    <Router>
      <Switch>
        <Route exact path="../../index.html" component={Component1} />
        <Route path="../../result/result.html" component={Component2} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  );
}

export default Routes;