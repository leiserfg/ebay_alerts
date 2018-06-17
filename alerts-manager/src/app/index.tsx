import * as React from 'react'
import {hot} from 'react-hot-loader'
import {Router, Route, Switch} from 'react-router'
import {Root} from 'app/containers/Root'
import {CreateAlertPage} from 'app/containers/CreateAlertPage'
import {AlertApp} from 'app/containers/AlertApp'

// render react DOM
export const App = hot(module)(({history}) => (
  <Root>
    <Router history={history}>
      <Switch>
        <Route path="/customer/:id" component={AlertApp} />
        <Route path="/" component={CreateAlertPage} />
      </Switch>
    </Router>
  </Root>
))

// <Route path="/" component={TodoApp} />
