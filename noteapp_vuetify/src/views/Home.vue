<template>
<v-app theme="dark">
  <v-btn @click="createNote()">Add note</v-btn>
  <v-container>
    <v-row
      v-masonry
      origin-left="true"
      transition-duration="0.3s"
      item-selector=".item"
      :order="order"
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
        <router-link style="text-decoration: none; color: inherit;" :to="`/note/${note.id}`">
            <v-card :elevation="isHovering ? 4 : 2"
            variant = "tonal" 
            color="blue-grey-lighten-4" 
            v-bind="props" 
            @click="v-ripple"
            @contextmenu.prevent.native="showContextMenu($event, note)"
            >
              
              <v-card-title>{{ note.title }}</v-card-title>
              <v-card-text>
                <div 
                v-for = "line in note.body.split('\n')">
                  {{ line }}
                </div>
              </v-card-text>
              <v-card-subtitle class="text-right text-padding" padding="2">{{ note.created.substring(0, note.created.indexOf("T")) }}</v-card-subtitle>
            </v-card>
          </router-link>
          </v-hover>


        </v-col>
      </v-row>
      <context-menu
        :x="menuPos.x"
        :y="menuPos.y"
        :items="menuItems"
        ref="contextMenu"
        @item-click="onMenuItemClick"
        />
    </v-container>
  </v-app>

</template>

<script>
import axios from 'axios'
import VueCookies from 'vue-cookies'
import ContextMenu from '../components/ContextMenu.vue'

export default{
  name: 'Notes',
  components: {
    ContextMenu,
  },
  data(){
    return{
      notes: {},
      order: {},
      menuPos: {x:0, y:0},
      menuItems: [
        {title: 'Select', action: 'select'},
        {title: 'Delete', action: 'delete'},
      ],
      contextMenuNote: null,
      selectedNotes: {},
    }
  },
  mounted() {
    this.getNotes()
    document.title = 'Fancy Notes'
  },
  methods:{
    async getUserData(){
      const csrftoken = VueCookies.get('csrftoken')
      return await axios
        .get('/api/user', {headers: {'Authorization': `Token ${csrftoken}`}})
        .then(response =>{
          //console.log(response.data)
          return response.data
        })
    },
    //get notes
    async getNotes(){
      const csrftoken = VueCookies.get('csrftoken')
      await axios
        .get('/api/notes/', {headers: {'Authorization': `Token ${csrftoken}`}})
        .then(response=> {
          this.notes = response.data
          
          // for (let i = 0; i < this.notes.length; i++) {
          //   this.notes[i].body = this.notes[i].body.replace("\n/g", "`<br>`")
          // }
          // this.notes.forEach(note => {
          //   console.log(note.body)
          // })

          //seems to do nothing in v-masonry :order='order'
          this.order = this.notes
            .sort((a, b) => new Date(b.created) - new Date(a.created))
            .map(note => note.id)
        })
        .catch(error => {
          console.log(error)
        })
    },
    //create note
    async createNote(){
      const user = await this.getUserData()
      const user_id = user['id']
      const csrftoken = VueCookies.get('csrftoken')
      await axios
        .post('/api/notes/', {title: '', body: '', user: user_id}, {headers: {'Authorization': `Token ${csrftoken}`}}) //temporaly id of admin user
        .then(response=>{
          const note_id = response.data.id;
          
          return this.$router.push(`/new-note/${note_id}`)
        })
        .catch(error=>{
          console.log(error)
        })
    }, 
    //delete note
    async deleteNote(){
      const csrftoken = VueCookies.get('csrftoken')
      const noteId = this.contextMenuNote.id;
      if (confirm("Are you sure?")){
        await axios
          .delete(`/api/notes/${noteId}/`, {headers: {'Authorization': `Token ${csrftoken}`}})
          .then(response => {
            console.log(response);
            this.notes = this.notes.filter(note => note.id !== noteId);
            this.$nextTick(() => this.$redrawVueMasonry());
          })
          .catch(error => {
          console.log(error)
        })
      }
    },

    //TODO selecting notes
    selectNote(){

    },

    //context menu
    showContextMenu(event, note) {
      //event.preventDefault(); //is it have to be here?
      this.contextMenuNote = note;
      this.menuPos = {x: event.clientX, y: event.clientY};
        this.$nextTick(() => {
          this.$refs.contextMenu.showMenu = true;
        });
    },
    //context menu actions
    onMenuItemClick(item) {
      if (item.action == "delete"){
        this.deleteNote()
      }
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