import * as React from 'react'
import {AlertTextInput} from 'app/components/AlertTextInput'
import AlertModel from 'app/models/AlertModel'

export interface HeaderProps {
  addAlert: (alert: Partial<AlertModel>) => any
}

export interface HeaderState {
  /* empty */
}

export class Header extends React.Component<HeaderProps, HeaderState> {
  private handleSave = (search_terms: string) => {
    if (search_terms.length) {
      this.props.addAlert({search_terms})
    }
  }

  render() {
    return (
      <header>
        <h1>Alerts</h1>
        <AlertTextInput
          newAlert
          onSave={this.handleSave}
          placeholder="What needs to be done?"
        />
      </header>
    )
  }
}

export default Header
