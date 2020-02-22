import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import Index from '@/views/Index.vue'

describe('views/Index.vue', () => {
  it('help text when no room entered', () => {
    const wrapper = shallowMount(Index, {})
    expect(wrapper.text()).to.include('Enter a room to chat')
  })
})
