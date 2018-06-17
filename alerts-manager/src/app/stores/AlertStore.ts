import {observable, action} from 'mobx'
import {AlertModel} from 'app/models'
import {AlertsApi, CreateAlert, CustomersApi} from '../client'

export class AlertStore {
  private alertsApi = new AlertsApi()
  private customersApi = new CustomersApi()

  @observable public alerts: Array<AlertModel>
  @observable public owner_id: string = null
  @observable public owner_email: string = null

  @action
  async addAlert(item: CreateAlert) {
    await this.alertsApi.alertsCreate(item)
    await this.fetchAlerts()
  }

  @action
  async fetchCustomer(customer_id: string) {
    this.owner_id = customer_id
    let customer = await this.customersApi.customersRead(customer_id)
    this.owner_email = customer.email
    await this.fetchAlerts()
  }

  @action
  async fetchAlerts() {
    const alerts = await this.alertsApi.alertsList(this.owner_id)
    this.alerts = alerts.map(a => a as AlertModel)
  }

  @action
  async editAlert(id: string, data: AlertModel) {
    const changedIndex = this.alerts.findIndex(it => it.id == id)
    if (changedIndex !== -1) {
      const updated = await this.alertsApi.alertsPartialUpdate(id, data)
      this.alerts[changedIndex] = updated as AlertModel
    }
  }

  @action
  async deleteAlert(id: string) {
    this.alerts = this.alerts.filter(alert => alert.id !== id)
    await this.alertsApi.alertsDelete(id)
  }

  // @action
  // enableAll = (): void => {
  //   this.alerts = this.alerts.map(alert => ({...alert, enabled: true}))
  // }

  // @action
  // disableAll = (): void => {
  //   this.alerts = this.alerts.map(alert => ({...alert, enabled: false}))
  // }

  // @action
  // clearDisabled = (): void => {
  //   this.alerts = this.alerts.filter(alert => !alert.enabled)
  // }
}

export default AlertStore
