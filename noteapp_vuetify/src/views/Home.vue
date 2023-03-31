<template>
<v-app theme="dark">
  <v-container>
    <v-row
      v-masonry
      origin-left="true"
      transition-duration="0.3s"
      item-selector=".item"
    >

      <v-col
        v-masonry-tile
        class="item"          
        v-for = "note in notes"
        v-bind:key = "note.id"
        xs="2"
        sm="6"
        md="3"
        lg="3"
      > 

      <v-hover
        v-slot="{ isHovering, props }"
        open-delay="20"
      >
            <v-card :elevation="isHovering ? 4 : 2"
            variant = "tonal" 
            color="blue-grey-lighten-4" 
            v-bind="props" 
            @click="v-ripple"
            >
              
              <v-card-title>{{ note.title }}</v-card-title>
              <v-card-text >{{ note.body }}</v-card-text>
              <v-card-subtitle class="text-right text-padding" padding="2">{{ note.created }}</v-card-subtitle>
            </v-card>

          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </v-app>

</template>

<script>
import axios from 'axios'
export default{
  name: 'Notes',
  data(){
    return{
      notes: {}
    }
  },
  mounted() {
    this.getNotes()
    document.title = 'Fancy Notes'
  },
  methods:{
    async getNotes(){
      await axios
        .get('/api/notes')
        .then(response=> {
          this.notes = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
}

</script>

<style>
.v-layout{
  background-color: #121212;
  box-sizing: border-box;
  padding: 0px;
  margin: 0px;
}
.v-container{
  padding: 15px;
  margin: 0px;
  width: 100%;
}
.text-padding {
  padding-bottom: 7px;
  padding-right: 9px;
  padding-left: 10;
  padding-top: 7px;
}

.v-title-padding {
  padding-bottom: 32px;
}

</style>