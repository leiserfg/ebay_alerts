import {observable, action, runInAction} from 'mobx'
import {AlertModel} from 'app/models'
import {AlertsApi, CreateAlert, CustomersApi} from '../client'

export class AlertStore {
  private alertsApi = new AlertsApi()
  private customersApi = new CustomersApi()

  @observable public alerts: Array<AlertModel> = []
  @observable public owner_id: string = null
  @observable public owner_email: string = null

  @action
  addAlert = async (item: CreateAlert) => {
    let newAlert = {email: this.owner_email, ...item}
    await this.alertsApi.alertsCreate(newAlert)
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
    runInAction(() => (this.alerts = alerts as AlertModel[]))
  }

  @action
  editAlert = async (id: string, data: AlertModel) => {
    const changedIndex = this.alerts.findIndex(it => it.id == id)
    if (changedIndex !== -1) {
      const updated = await this.alertsApi.alertsPartialUpdate(id, data)
      runInAction(() => {
        this.alerts[changedIndex] = updated as AlertModel
      })
    }
  }

  @action
  deleteAlert = async (id: string) => {
    this.alerts = this.alerts.filter(alert => alert.id !== id)
    await this.alertsApi.alertsDelete(id)
  }
}

export default AlertStore
