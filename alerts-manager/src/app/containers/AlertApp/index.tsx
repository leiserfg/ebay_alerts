import * as React from 'react'
import * as style from './style.css'
import {inject, observer} from 'mobx-react'
import {RouteComponentProps} from 'react-router'
import {AlertStore} from 'app/stores'
import {STORE_ROUTER, STORE_ALERT} from 'app/constants'

export interface AlertAppProps extends RouteComponentProps<any> {}

export interface AlertAppState {}

@inject(STORE_ALERT, STORE_ROUTER)
@observer
export class AlertApp extends React.Component<AlertAppProps, AlertAppState> {
  alert: AlertStore
  constructor(props: AlertAppProps, context: any) {
    super(props, context)
    this.alert = this.props[STORE_ALERT]
  }

  componentWillMount() {
    this.alert.fetchCustomer(this.props.match.params.id)
  }

  // const alertStore = this.props[STORE_ALERT] as AlertStore
  render() {
    const {children} = this.props

    return <div className={style.normal}>{children}</div>
  }
}

// <AlertList
//   deleteAlert={todoStore.deleteAlert}
//   editAlert={todoStore.editAlert}
// />
// <Header addAlert={todoStore.addAlert} />
