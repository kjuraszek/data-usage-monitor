import { createLocalVue, mount } from "@vue/test-utils"
import Vuetify from "vuetify"
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import Main from "@/partials/Main.vue"
import { Home, Settings, NotFound } from "@/views"
import routes from '@/router/routes'

describe("Main.vue Test", () => {
  const localVue = createLocalVue()
  localVue.use(Vuex)
  localVue.use(VueRouter)
  let router
  let store
  let vuetify

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
    router = new VueRouter({
      mode: 'history',
      routes,
    })
  })

  it("renders main", () => {
    const wrapper = mount(Main, {
      localVue,
      router,
      vuetify,
      store
    })
    expect(wrapper.vm.$options.name).toMatch("Main")
    expect(wrapper.find(".v-main").exists()).toBe(true)
    expect(wrapper.vm.$route.path).toBe("/")
  })

  it("renders Home component depending on route", async () => {
    const wrapper = mount(Main, {
      localVue,
      router,
      vuetify,
      store
    })

    expect(wrapper.vm.$route.path).toBe("/")
    expect(wrapper.findComponent( Home ).exists()).toBe(true)
  })

  it("renders Settings component depending on route", async () => {
    const wrapper = mount(Main, {
      localVue,
      router,
      vuetify,
      store
    })
    
    await router.push("/settings")
    await wrapper.vm.$nextTick()
    
    expect(wrapper.vm.$route.path).toBe("/settings")
    expect(wrapper.findComponent( Settings ).exists()).toBe(true)
  })

  it("renders NotFound component depending on route", async () => {
    const wrapper = mount(Main, {
      localVue,
      router,
      vuetify,
      store
    })
    
    await router.push("/path-doesnt-exist")
    await wrapper.vm.$nextTick()
    
    expect(wrapper.vm.$route.path).toBe("/path-doesnt-exist")
    expect(wrapper.findComponent( NotFound ).exists()).toBe(true)
  })
})
