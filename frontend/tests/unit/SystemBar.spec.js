import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import SystemBar from "@/partials/SystemBar.vue"

describe("SystemBar.vue Test", () => {
  const localVue = createLocalVue()
  let vuetify
  beforeEach(() => {
    vuetify = new Vuetify()
  })

  it("renders SystemBar with icon and text", () => {
    const wrapper = mount(SystemBar, {
      localVue,
      vuetify,
    })
    expect(wrapper.vm.$options.name).toMatch("SystemBar")
    expect(wrapper.find(".v-system-bar").exists()).toBe(true)
    expect(wrapper.find(".v-icon").exists()).toBe(true)
    expect(wrapper.find("span").exists()).toBe(true)
  })
})
