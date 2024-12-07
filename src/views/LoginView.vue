<template>
    <h1>Login</h1>
    <div>
      <input type="text" placeholder="Email" v-model="email"/> <br><br>
      <input type="password" placeholder="Password" v-model="password"/> <br> <br>
      <button @click="submitLogin">Login</button>
    </div>
</template>

<script>
export default {
  name:"Login",

  data(){
    return{
      email:'',
      password:'',
    }
  },
  methods:{
      async submitLogin(){
        const url = 'http://127.0.0.1:5000/login';
        const userData = { 'email': this.email, 'password': this.password };

        const response=await fetch(url, {
          method:'POST',
          headers: {'Content-Type': 'application/json',},
          body: JSON.stringify(userData),
        });

        this.email=''
        this.password=''        

        if(response.ok){
          const data=await response.json()
          console.log(data);
        }
      }
  },
}
</script>

<style>

</style>
