<template>
  <v-app>
    <h3>Home view</h3>
    <v-card>
      <v-row justify='center' :gutter="20" >
          <v-col          
          v-for = "note in notes"
          v-bind:key = "note.id"
          v-bind:note = "note" >
            <v-card variant = "tonal">
              <v-card-title>{{ note.title }}</v-card-title>
              <v-card-text>{{ note.body }}</v-card-text>
            </v-card>
        </v-col>
      </v-row>
    </v-card>
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
