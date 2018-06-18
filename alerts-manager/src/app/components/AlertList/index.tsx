import * as React from 'react'
import {AlertItem, AlertActions} from 'app/components/AlertItem'
import AlertModel from 'app/models/AlertModel'
import * as style from './style.css'

import {observer} from 'mobx-react'
export interface AlertListProps extends AlertActions {
  alerts: AlertModel[]
}

export interface AlertListState {}

@observer
export class AlertList extends React.Component<AlertListProps, AlertListState> {
  constructor(props?: AlertListProps, context?: any) {
    super(props, context)
  }

  private handleToggleAll = (e: React.SyntheticEvent<any>) => {
    e.preventDefault()
  }

  renderToggleAll() {
    const {alerts} = this.props
    const completedCount = alerts.length
    if (alerts.length > 0) {
      return (
        <input
          className={style.toggleAll}
          type="checkbox"
          checked={completedCount === alerts.length}
          onChange={this.handleToggleAll}
        />
      )
    }
  }

  render() {
    const {alerts, ...actions} = this.props
    return (
      <section className={style.main}>
        {this.renderToggleAll()}
        <ul className={style.normal}>
          {alerts.map(alert => (
            <AlertItem key={alert.id} alert={alert} {...actions} />
          ))}
        </ul>
      </section>
    )
  }
}

export default AlertList
