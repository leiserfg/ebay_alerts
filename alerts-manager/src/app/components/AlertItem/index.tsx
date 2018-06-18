import * as React from 'react'
import * as classNames from 'classnames'
import {AlertTextInput} from 'app/components/AlertTextInput'
import AlertModel from 'app/models/AlertModel'
import * as style from './style.css'

export interface AlertActions {
  editAlert: (id: string, data: Partial<AlertModel>) => any
  deleteAlert: (id: string) => any
}

export interface AlertProps extends AlertActions {
  alert: AlertModel
}

export interface AlertState {
  editing: boolean
}

export class AlertItem extends React.Component<AlertProps, AlertState> {
  constructor(props?: AlertProps, context?: any) {
    super(props, context)
    this.state = {editing: false}
  }

  private handleDoubleClick = (e: React.SyntheticEvent<any>) => {
    this.setState({editing: true})
  }

  private handleToggleCheckbox = (e: React.SyntheticEvent<any>) => {
    const {alert} = this.props
    const target = e.target as any
    if (
      target &&
      target.checked !== undefined &&
      target.checked !== alert.enabled
    ) {
      this.updateAlert({enabled: target.checked})
    }
  }

  private handleClickDeleteButton = (e: React.SyntheticEvent<any>) => {
    const {alert, deleteAlert} = this.props
    deleteAlert(alert.id)
  }

  private updateAlert = (data: Partial<AlertModel>) => {
    const {alert} = this.props
    if (
      data.search_terms !== undefined &&
      data.search_terms.trim().length === 0
    ) {
      this.props.deleteAlert(alert.id)
    } else {
      this.props.editAlert(alert.id, data)
    }
    this.setState({editing: false})
  }

  render() {
    const {alert} = this.props

    const element = this.state.editing ? (
      <AlertTextInput
        search_terms={alert.search_terms}
        editing={this.state.editing}
        onSave={search_terms => this.updateAlert({search_terms})}
      />
    ) : (
      <div className={style.view}>
        <input
          className={style.toggle}
          type="checkbox"
          checked={alert.enabled}
          onChange={this.handleToggleCheckbox}
        />

        <label onDoubleClick={this.handleDoubleClick}>
          {alert.search_terms}
        </label>

        <button
          className={style.destroy}
          onClick={this.handleClickDeleteButton}
        />
      </div>
    )

    const classes = classNames({
      [style.enabled]: alert.enabled,
      [style.editing]: this.state.editing,
      [style.normal]: !this.state.editing
    })

    return <li className={classes}>{element}</li>
  }
}

export default AlertItem
