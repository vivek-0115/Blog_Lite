<template>
    <h1>Register</h1>
    <div>
      <input type="text" placeholder="Email" v-model="email"/> <br><br>
      <input type="password" placeholder="Password" v-model="password"/> <br> <br>
      <input type="text" placeholder="Role:user only" v-model="role"/> <br><br>
      <button @click="registerLogin">Register</button>
    </div>
</template>

<script>
export default {
    name:"Register",

    data(){
        return{
            email:'',
            password:'',
            role:'',
        }
    },
    methods:{
        async registerLogin(){
        const url = 'http://127.0.0.1:5000/register';
        const userData = { 'email': this.email, 'password': this.password, 'role':this.role };

        const response=await fetch(url, {
          method:'POST',
          headers: {'Content-Type': 'application/json',},
          body: JSON.stringify(userData),
        });

        this.role='',
        this.email=''
        this.password=''

        if(response.ok){
          const data=await response.json()
          console.log(data);
        }
      }
    }
}
</script>

<style>

</style>