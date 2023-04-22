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
            <v-btn @click="signUp()">Sign Up</v-btn>
        </v-form>
        <br>
        <router-link to="/login">Login instead</router-link>
    </v-app>
</template>

<script>
import axios from 'axios'

export default{
    name: 'SignUp',
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
                value => {
                    if (value?.length >= 3) return true

                    return 'Minimum 3 characters.'
                },
            ],
            passwordRules: [
                value => {
                    if (value) return true

                    return 'Name is requred.'
                },
                value => {
                    if (value?.length >= 8) return true

                    return 'Minimum 8 characters.'
                },
            ],
        }
    },
    methods: {
        async signUp(){
            const username = this.username;
            const password = this.password;

            await axios
                .post('/api/sign-up/', {username: username, password: password})
                .then(response =>{
                    console.log(response.data)
                    return this.$router.push(`/login`)
                })
                .catch(error=>{
                    console.log(error)
                })
        }
    }
}
</script>