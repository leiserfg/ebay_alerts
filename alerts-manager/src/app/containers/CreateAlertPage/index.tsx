import * as React from 'react'
import * as style from './style.css'
import {AlertsApi} from '../../client'

const api = new AlertsApi()

export interface CreateAlertPageState {
  email: string
  search_terms: string
  frequency: number
}
export interface CreateAlertPageProps {}

export class CreateAlertPage extends React.Component<
  CreateAlertPageProps,
  CreateAlertPageState
> {
  constructor(props: CreateAlertPageProps, context: any) {
    super(props, context)
    this.state = {
      email: '',
      search_terms: '',
      frequency: 10
    }
  }

  handleSubmit = event => {
    event.preventDefault()

    if (!this.state.email.match(/.*@.*/)) {
      alert('The email is invalid')
      return
    }
    if (!this.state.search_terms.trim()) {
      alert('The search_terms cannot be empty')
      return
    }

    api
      .alertsCreate(this.state)
      .then(() => alert('Check your email for confirmation'))
      .catch(e => alert(e.message))
  }

  handleInputChange = event => {
    const target = event.target
    const value = target.type === 'checkbox' ? target.checked : target.value
    const name = target.name
    this.setState({
      [name]: value
    } as any)
  }

  render() {
    return (
      <div className={style.normal}>
        <h1>Create Alert</h1>
        <form onSubmit={this.handleSubmit}>
          <label>
            Email:{' '}
            <input
              name="email"
              value={this.state.email}
              onChange={this.handleInputChange}
            />
          </label>

          <label>
            Search Term:{' '}
            <input
              name="search_terms"
              value={this.state.search_terms}
              onChange={this.handleInputChange}
            />{' '}
          </label>

          <label>
            Frequency:
            <select
              value={this.state.frequency}
              name="frequency"
              onChange={this.handleInputChange}
            >
              <option value="2">For every 2 mins</option>
              <option value="10">For every 10 mins</option>
              <option value="30">For every 30 mins</option>
            </select>
          </label>
          <button> Create </button>
        </form>
      </div>
    )
  }
}
