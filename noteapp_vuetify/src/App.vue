<template>
  <v-app theme="dark">
  <v-card>
    <v-layout>
      <!-- <v-navigation-drawer
        image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        permanent
        theme="dark"
      > -->
      <v-navigation-drawer
        permanent
        theme="dark"
        color="#0F8C52"
        class="border-thin"
        :border="0"
        elevation="5"
        :width="230"
      >
        <v-list nav>
          <h1>Fancy Notes</h1>
          <v-divider></v-divider>
          <div class="text-subtitle-1" v-if="username.length > 0">Hello {{username}}!</div>
          <router-link v-if="username == ''" to="/login">
          <div class="text-subtitle-1">Login</div>
          </router-link>
          
          <router-link style="text-decoration: none; color: inherit;" to="/">
          <v-list-item prepend-icon="mdi-notebook" title="Notes" value="notes"></v-list-item>
          </router-link>
          
          <v-list-item prepend-icon="mdi-cog" title="Settings" value="settings"></v-list-item>
          
          <v-list-item v-if="username.length > 0" title="Logout" value="logout" @click="logout()"></v-list-item>
          
          <router-link style="text-decoration: none; color: inherit;" to="/recycle-bin">
          <v-list-item v-if="username.length > 0" title="RecycleBin" value="recycle-bin"></v-list-item>
          </router-link>

        </v-list>
      </v-navigation-drawer>
      

      <v-main>
        <v-container align-center>
          <router-view />
        </v-container>
      </v-main>


    </v-layout>

  </v-card>

</v-app>
</template>

<script setup>
import Home from './views/Home.vue';
</script>

<script>
import axios from 'axios'
import VueCookies from 'vue-cookies'
export default{
  name: 'App',
  data(){
    return{
      username: '',
    }
  },
  async mounted() {
    const user_data = await this.getUserData()
    this.username = user_data['username']
    console.log(this.username)
    document.title = 'Fancy Notes'
  },
  methods:{
    async getUserData(){
      const csrftoken = VueCookies.get('csrftoken')
      return await axios
        .get('/api/user/', {headers: {'Authorization': `Token ${csrftoken}`}})
        .then(response =>{
          console.log(response.data)
          return response.data
        })
    },
    async logout(){
      const csrftoken = VueCookies.get('csrftoken')
      await axios
        .post('/api/logout/', {}, {headers: {'Authorization': `Token ${csrftoken}`}})
        .then(response => {
          this.$router.push('/')
          location.reload()
        })
        .catch(error =>{
          console.log(error)
        })
    },
  },
}
</script>
<style>

</style>