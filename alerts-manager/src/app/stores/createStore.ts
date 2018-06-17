import {History} from 'history'
import {AlertStore} from './AlertStore'
import {RouterStore} from './RouterStore'
import {STORE_ALERT, STORE_ROUTER} from 'app/constants'

export function createStores(history: History) {
  const routerStore = new RouterStore(history)
  const alertStore = new AlertStore()

  return {
    [STORE_ROUTER]: routerStore,
    [STORE_ALERT]: alertStore
  }
}
