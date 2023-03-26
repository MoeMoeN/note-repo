<template>
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
        color="#750409"
      >
        <v-list nav>
          <h2>Fancy Notes</h2>
          <v-list-item prepend-icon="mdi-notebook" title="Notes" value="notes"></v-list-item>
          <v-list-item prepend-icon="mdi-cog" title="Settings" value="settings"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      
      <v-main>
        <v-container align-center>
          <router-view />
        </v-container>
      </v-main>
      


    </v-layout>
  </v-card>


</template>

<script setup>
  //
</script>
