import * as React from 'react'
import * as style from './style.css'
import {inject, observer} from 'mobx-react'
import {RouteComponentProps} from 'react-router'
import {AlertStore} from 'app/stores'
import {STORE_ROUTER, STORE_ALERT} from 'app/constants'
import {AlertList, Header} from 'app/components/'

export interface AlertAppProps extends RouteComponentProps<any> {}

export interface AlertAppState {}

@inject(STORE_ALERT, STORE_ROUTER)
@observer
export class AlertApp extends React.Component<AlertAppProps, AlertAppState> {
  alertStore: AlertStore
  constructor(props: AlertAppProps, context: any) {
    super(props, context)
    this.alertStore = props[STORE_ALERT]
  }

  componentWillMount() {
    const id = '90c1a50c-7287-11e8-a91c-0242ac120005' // this.props.match.params.id
    this.alertStore.fetchCustomer(id)
  }

  // const alertStore = this.props[STORE_ALERT] as AlertStore
  render() {
    const {children} = this.props

    return (
      <div className={style.normal}>
        <Header addAlert={this.alertStore.addAlert} />
        <AlertList
          deleteAlert={this.alertStore.deleteAlert}
          editAlert={this.alertStore.editAlert}
          alerts={this.alertStore.alerts}
        />
        {children}
      </div>
    )
  }
}

// <AlertList
//   deleteAlert={todoStore.deleteAlert}
//   editAlert={todoStore.editAlert}
// />
// <Header addAlert={todoStore.addAlert} />
