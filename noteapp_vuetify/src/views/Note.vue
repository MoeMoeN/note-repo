<template>
<v-app theme="dark">
    <v-form @submit.prevent>
        <v-container>
                <v-text-field
                id="title"
                v-model="note.title"
                hide-details
                single-line
                ></v-text-field>
                        
                <v-divider></v-divider>
            <v-textarea
            id="body"
            counter
            autofocus
            no-resize
            rows="23"
            v-model="note.body"
            >
            </v-textarea>
            <v-btn @click="saveNote()">Save</v-btn>
        </v-container>
    </v-form>
</v-app>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Note',
    data(){
        return{
            note: {},
        }
    },
    mounted(){
        this.getNote()
        
    },
    methods: {
        async getNote(){
            const note_id = this.$route.params.note_id;
            await axios
                .get(`/api/notes/${note_id}`)
                .then(response => {
                    this.note = response.data
                    //console.log(this.note)
                    document.title = this.note.title + " | Fancy Notes"
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async saveNote(){
            const note_title = this.note.title
            const note_body = this.note.body
            const note_id = this.$route.params.note_id;
            //TODO save functionality
            //send post request to django
            //with new title and body
            await axios
                .post(`/api/notes/${note_id}/`, {title: note_title, body: note_body})
                .then(response => {
                    //console.log(response)
                })
                .catch(error=>{
                    console.log(error)
                })
        }

    }
}
</script>