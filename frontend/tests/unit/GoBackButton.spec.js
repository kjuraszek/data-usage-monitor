import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import VueRouter from 'vue-router'
import GoBackButton from "@/partials/GoBackButton.vue"
import routes from '@/router/routes'

describe("GoBackButton.vue Test", () => {
  const localVue = createLocalVue()
  localVue.use(VueRouter)
  let router
  let vuetify

  beforeEach(() => {
    router = new VueRouter({
      mode: 'history',
      routes
    })
    vuetify = new Vuetify()
  })

  it("renders button", () => {
    const wrapper = mount(GoBackButton, {
      localVue,
      router,
      vuetify
    })
    expect(wrapper.vm.$options.name).toMatch("GoBackButton")
    expect(wrapper.find(".v-btn").exists()).toBe(true)
  })

  it("changes route on button click", async () => {
    const wrapper = mount(GoBackButton, {
      localVue,
      router,
      vuetify
    })

    await wrapper.find(".v-btn").trigger('click')
    await wrapper.vm.$nextTick()

    expect(wrapper.vm.$route.path).toMatch("/")
  })
})
