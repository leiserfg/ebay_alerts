import {observable} from 'mobx'

export default class AlertModel {
  readonly id: string
  @observable public search_terms: string
  @observable public enabled: boolean
  @observable public frequency: number
}
