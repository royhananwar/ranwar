import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import HelloWorld from './components/HelloWorld.vue'
import HomePage from './components/Blog/HomePage.vue'

Vue.use(VueRouter)

const routes = [
    { 
        path: '/hello', 
        component: HelloWorld 
    },
    {
        path: '/',
        component: HomePage 
    },
]

const router = new VueRouter({
    routes, // short for routes: routes
    mode: 'history'
})

new Vue({
    el: '#app',
    components: { App },
    router,
    render: h => h(App)
})
