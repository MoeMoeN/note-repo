/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import { loadFonts } from './webfontloader'
import vuetify from './vuetify'
import pinia from '../store'
import router from '../router'


import { vue3Debounce } from 'vue-debounce'
import { VueMasonryPlugin } from 'vue-masonry'

export function registerPlugins (app) {
  loadFonts()
  app
    .use(vuetify)
    .use(pinia)
    .use(router)
    .use(VueMasonryPlugin)
    .directive('debounce', vue3Debounce({ lock: true }))
}
