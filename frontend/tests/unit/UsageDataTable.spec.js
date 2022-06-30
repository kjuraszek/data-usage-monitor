import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import Vuex from 'vuex'
import UsageDataTable from "@/partials/UsageDataTable.vue"

describe("UsageDataTable.vue Test", () => {
  const localVue = createLocalVue()
  localVue.use(Vuex)
  let vuetify
  let store
  beforeEach(() => {
    vuetify = new Vuetify()
    store = new Vuex.Store({
      state: {
        loading: true,
        failed: false,
        autoRefresh: false,
        darkMode: false,
        currentMonthDownload: 0.0,
        currentMonthUpload: 0.0,
        currentTimeStamp: null,
      }
    })
  })

  it("renders UsageDataTable with paragraph and v-simple-table", () => {
    const wrapper = mount(UsageDataTable, {
      localVue,
      vuetify,
      store
    })
    expect(wrapper.vm.$options.name).toMatch("UsageDataTable")
    expect(wrapper.find(".v-data-table").exists()).toBe(true)
    expect(wrapper.find("p.text-h6").exists()).toBe(true)
  })
})
