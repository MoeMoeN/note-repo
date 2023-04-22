<template>
    <v-app theme="dark">
        <v-form v-model="valid">
            <v-container>
                <v-row>
                    <v-text-field
                    v-model="username"
                    :rules="nameRules"
                    label="Username"
                    required
                    ></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field
                    type="password"
                    v-model="password"
                    :rules="passwordRules"
                    label="Password"
                    required
                    ></v-text-field>
                </v-row>
            </v-container>
            <v-btn @click="login()">Login</v-btn>
        </v-form>
        <br>
        <router-link to="/sign-up">Sign up instead</router-link>
    </v-app>
</template>

<script>
import axios from 'axios'
import VueCookies from 'vue-cookies'

export default{
    name: 'Login',
    data(){
        return{
            valid: false,
            username: '',
            password: '',
            
            nameRules: [
                value => {
                    if (value) return true

                    return 'Name is requred.'
                },
            ],
            passwordRules: [
                value => {
                    if (value) return true

                    return 'Name is requred.'
                },
            ],
        }
    },
    methods: {
        async login(){
            const username = this.username;
            const password = this.password;

            await axios
                .post('/api/login/', {username: username, password: password})
                .then(response =>{
                    const csrftoken = response.data['token']
                    VueCookies.set('csrftoken', csrftoken)
                    console.log(response.data)
                    return this.$router.push(`/`).then(()=>{location.reload()})
                })
                .catch(error=>{
                    console.log(error)
                    //console.log(csrftoken)
                })
        }
    }
}
</script>