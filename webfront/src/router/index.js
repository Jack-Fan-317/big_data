import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import test from '@/components/test'
// import wstest from '@/components/wstest'


// import LeftChart from '@/components/LeftChart'
// import LeftChart2 from '@/components/LeftChart2'
// import MiddleChart1 from '@/components/MiddleChart1'
import index from '@/components/datav/index'
import test from '@/components/datav/test'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    // {
    //   path: '/test',
    //   name: 'test',
    //   component: test
    // },
    // {
    //   path: '/wstest',
    //   name: 'wstest',
    //   component: wstest
    // },
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/test',
      name: 'test',
      component: test
    }
  ]
})
