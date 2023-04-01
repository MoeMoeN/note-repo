<template>
    <v-container>
        <v-card>
            <v-card-title>{{ note.title }}</v-card-title>
            <v-card-text>{{ note.body }}</v-card-text>
        </v-card>
    </v-container>
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
                    console.log(this.note)
                    document.title = this.note.title + " | Fancy Notes"
                })
                .catch(error => {
                    console.log(error)
                })
        }

    }
}
</script>