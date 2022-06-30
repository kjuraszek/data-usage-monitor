import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import Loader from "@/partials/Loader.vue"

describe("Loader.vue Test", () => {
  const localVue = createLocalVue()
  let vuetify
  beforeEach(() => {
    vuetify = new Vuetify()
  })

  it("renders loader and paragraph with text when passed", () => {
    const loadingText = "Examplary loading text"
    const wrapper = mount(Loader, {
      localVue,
      vuetify,
      propsData: {
        text: loadingText
      }
    })
    expect(wrapper.vm.$options.name).toMatch("Loader")
    expect(wrapper.find(".v-progress-circular").exists()).toBe(true)
    expect(wrapper.find("p.text-subtitle-2").exists()).toBe(true)
    expect(wrapper.text()).toMatch(loadingText)
  })

  it("doesn't render paragraph when text not passed", () => {
    const wrapper = mount(Loader, {
      localVue,
      vuetify
    })
    expect(wrapper.vm.$options.name).toMatch("Loader")
    expect(wrapper.find(".v-progress-circular").exists()).toBe(true)
    expect(wrapper.find("p.text-subtitle-2").exists()).toBe(false)
    expect(wrapper.text()).toMatch("")
  })
})
