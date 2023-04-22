<template>
    <v-app theme="dark">
        <v-form @submit.prevent>
            <v-container>
                <v-textarea
                id="body"
                counter
                autofocus
                no-resize
                rows="23"
                v-model="note.body"
                v-debounce:5s="saveNote"
                >
                </v-textarea>
                <v-btn @click="saveNote()">Save</v-btn>
                <v-progress-circular v-show="isLoading" size="25" width="3" color="white" style="margin-left: 20px;" indeterminate></v-progress-circular>
        </v-container>
    </v-form>

    <v-snackbar
    v-model="snackbar_saved"
    :timeout="snackbar_timeout"
    color="success"
    location="bottom right"
    >
        Saved!
    </v-snackbar>
    </v-app>
</template>
    
<script>
import axios from 'axios'
import VueCookies from 'vue-cookies'
export default {
    name: 'Note',
    data(){
        return{
            note: {},
            snackbar_saved: false,
            snackbar_timeout: 2000,
            isLoading: false,
        }
    },
    mounted(){
        this.getNote()
                //capture ctrl + s
                this._keyListener = function(e) {
            if (e.key === "s" && (e.ctrlKey || e.metaKey)) {
                e.preventDefault(); // present "Save Page" from getting triggered.

                this.saveNote();
            }
        };

        document.addEventListener('keydown', this._keyListener.bind(this));
    },
    beforeDestroy() {
        document.removeEventListener('keydown', this._keyListener);
    },
    methods: {
        async getNote(){
            const csrftoken = VueCookies.get('csrftoken')
            const note_id = this.$route.params.note_id;
            await axios
                .get(`/api/notes/${note_id}`, {headers: {'Authorization': `Token ${csrftoken}`}})
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
            this.isLoading = true;
            this.snackbar_saved = false;
            const csrftoken = VueCookies.get('csrftoken')
            const note_body = this.note.body

            const firstLine = note_body.substring(0, note_body.indexOf('\n'));
            const note_title = firstLine.length > 50 ? firstLine.substring(0, 50) : firstLine;
            const note_id = this.$route.params.note_id;
            //TODO add auto save when inactive (stopped writing for some time)
            await axios
                .patch(`/api/notes/${note_id}/`, {title: note_title, body: note_body}, {headers: {'Authorization': `Token ${csrftoken}`}})
                .then(response => {
                    //console.log(response)
                    this.snackbar_saved = true;
                    this.isLoading = false;  
                })
                .catch(error=>{
                    console.log(error)
                })
        }

    }
}
</script>