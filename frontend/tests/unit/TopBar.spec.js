import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import TopBar from "@/partials/TopBar.vue"

describe("TopBar.vue Test", () => {
  const localVue = createLocalVue()
  localVue.use(Vuetify)
  let vuetify
  beforeEach(() => {
    vuetify = new Vuetify()
  })

  it("renders top bar", () => {
    const wrapper = mount(TopBar, {
      localVue,
      vuetify,
    })
    expect(wrapper.vm.$options.name).toMatch("TopBar")
    expect(wrapper.find(".v-app-bar").exists()).toBe(true)
    expect(wrapper.find(".v-image").exists()).toBe(true)
  })
})
