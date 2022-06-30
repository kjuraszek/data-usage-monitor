import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import Failed from "@/partials/Failed.vue"

describe("Failed.vue Test", () => {
  const localVue = createLocalVue()
  let vuetify
  beforeEach(() => {
    vuetify = new Vuetify()
  })

  it("renders paragraph with text when passed", () => {
    const failedText = "Examplary failed text"
    const wrapper = mount(Failed, {
      localVue,
      vuetify,
      propsData: {
        text: failedText
      }
    })
    expect(wrapper.vm.$options.name).toMatch("Failed")
    expect(wrapper.find(".v-icon").exists()).toBe(true)
    expect(wrapper.find("p.text-subtitle-2").exists()).toBe(true)
    expect(wrapper.text()).toMatch(failedText)
  })

  it("doesn't render paragraph when text not passed", () => {
    const wrapper = mount(Failed, {
      localVue,
      vuetify
    })
    expect(wrapper.vm.$options.name).toMatch("Failed")
    expect(wrapper.find(".v-icon").exists()).toBe(true)
    expect(wrapper.find("p.text-subtitle-2").exists()).toBe(false)
    expect(wrapper.text()).toMatch("")
  })
})
