import { shallowMount } from '@vue/test-utils'
import MainHeading from '@/partials/MainHeading.vue'

describe('MainHeading.vue Test', () => {
  it('renders props.msg when passed', () => {
    const title = 'Examplary heading Title'
    const wrapper = shallowMount(MainHeading, {
      propsData: {
        text: title
      }
    })
    expect(wrapper.vm.$options.name).toMatch('MainHeading')
    expect(wrapper.text()).toMatch(title)
  })
})
