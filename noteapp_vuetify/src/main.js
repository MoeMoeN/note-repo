/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

import axios from 'axios'

const app = createApp(App)

//set axios to be accessed globally and set default url
axios.defaults.baseURL = "http://127.0.0.1:8000"
app.config.globalProperties.$axios = axios


registerPlugins(app)

app.mount('#app')
