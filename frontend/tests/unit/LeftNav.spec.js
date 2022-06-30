import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import VueRouter from 'vue-router'
import LeftNav from "@/partials/LeftNav.vue"
import routes from '@/router/routes'

describe("LeftNav.vue Test", () => {
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

  it("renders left navigation", () => {
    const wrapper = mount(LeftNav, {
      localVue,
      router,
      vuetify
    })
    expect(wrapper.vm.$options.name).toMatch("LeftNav")
    expect(wrapper.find(".v-navigation-drawer").exists()).toBe(true)
    expect(wrapper.vm.$route.path).toBe("/")
  })

  it("changes route on unselected nav list item click", async () => {
    const wrapper = mount(LeftNav, {
      localVue,
      router,
      vuetify
    })
    let selectedItem = 1

    await wrapper.findAllComponents(".v-list-item").at(selectedItem).trigger('click')
    await wrapper.vm.$nextTick()
    expect(wrapper.vm.selectedItem).toBe(selectedItem)
    expect(wrapper.vm.$route.path).toBe("/settings")
  })

  it("doesn't change route on selected nav list item click", async () => {
    const wrapper = mount(LeftNav, {
      localVue,
      router,
      vuetify
    })
    let selectedItem = 0

    await wrapper.findAllComponents(".v-list-item").at(selectedItem).trigger('click')
    await wrapper.vm.$nextTick()
    expect(wrapper.vm.selectedItem).toBe(selectedItem)
    expect(wrapper.vm.$route.path).toBe("/")
  })
})
