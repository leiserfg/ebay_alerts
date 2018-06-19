import * as React from 'react'
import {AlertTextInput} from 'app/components/AlertTextInput'
import AlertModel from 'app/models/AlertModel'
import * as style from './style.css'


export interface HeaderProps {
  addAlert: (alert: Partial<AlertModel>) => any
}

export interface HeaderState {
  frequency: number
}

export class Header extends React.Component<HeaderProps, HeaderState> {
  constructor(props?: HeaderProps, context?: any) {
    super(props, context)
    this.state = {frequency: 10}
  }

  private handleSave = (search_terms: string) => {
    if (search_terms.length) {
      this.props.addAlert({search_terms, frequency: this.state.frequency})
    }
  }

  private handleFreqChange = (e: React.SyntheticEvent<any>) => {
    const target = e.target as any
    let frequency = parseInt(target.value)
    this.setState({frequency})
  }

  render() {
    return (
	    <header className={style.header}>
        <h1>Ebay Alerts</h1>
        <AlertTextInput
          newAlert
          onSave={this.handleSave}
          placeholder="What do yo wanna search for?"
        />

        <select onChange={this.handleFreqChange} value={this.state.frequency}>
          <option value="2">Every 2 mins</option>
          <option value="10">Every 10 mins</option>
          <option value="30">Every 30 mins</option>
        </select>
      </header>
    )
  }
}

export default Header
