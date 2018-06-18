import * as React from 'react'
import * as classNames from 'classnames'
import * as style from './style.css'

export interface AlertTextInputProps {
  search_terms?: string
  placeholder?: string
  newAlert?: boolean
  editing?: boolean
  onSave: (search_terms: string) => any
}

export interface AlertTextInputState {
  search_terms: string
}

export class AlertTextInput extends React.Component<
  AlertTextInputProps,
  AlertTextInputState
> {
  constructor(props?: AlertTextInputProps, context?: any) {
    super(props, context)
    this.state = {
      search_terms: this.props.search_terms || ''
    }
  }

  private handleSubmit = e => {
    const text = e.target.value.trim()
    if (e.which === 13) {
      this.props.onSave(text)
      if (this.props.newAlert) {
        this.setState({search_terms: ''})
      }
    }
  }

  private handleChange = e => {
    this.setState({search_terms: e.target.value})
  }

  private handleBlur = e => {
    const text = e.target.value.trim()
    if (!this.props.newAlert) {
      this.props.onSave(text)
    }
  }

  render() {
    const classes = classNames(
      {
        [style.edit]: this.props.editing,
        [style.new]: this.props.newAlert
      },
      style.normal
    )

    return (
      <input
        className={classes}
        type="text"
        autoFocus
        placeholder={this.props.placeholder}
        value={this.state.search_terms}
        onBlur={this.handleBlur}
        onChange={this.handleChange}
        onKeyDown={this.handleSubmit}
      />
    )
  }
}

export default AlertTextInput
