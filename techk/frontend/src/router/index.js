import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import listBook from '@/components/book/listBook'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/books',
      name: 'listBook',
      component: listBook
    }
  ],
  mode: 'history'
})
