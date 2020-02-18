<template>
  <div class="container">
    <div>
      <h1 class="title">
        Dynamic Client
      </h1>
      <h2 class="subtitle">
        Frontend with feature flag mechanism
      </h2>
      <br />
      <h2 class="subtitle">Please Login</h2>
      <form method="POST" @submit="checkForm">
        <input id="username" class="input-form" type="text" name="username" placeholder="Username" v-model="username" />
        <input id="password" class="input-form" type="password" name="password" placeholder="Password" v-model="password"/>
        <input class="btn btn-blue" type="submit"/>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      login_credential: {
        "username":"sam",
        "password":"quickbrownfox"
      },
      errors: [],
      username: '',
      password: ''
    }
  },
  mounted(){
    if (localStorage.username) {
      this.username = localStorage.username
    }
  },
  watch: {
    username(newUsername){
      localStorage.username = newUsername
    }
  },
  methods: {
    parseJwt: function(token) {
      try {
        return JSON.parse(atob(token.split('.')[1]));
      } catch (e) {
        console.log(e)
        return null;
      }
    },
    checkForm: function(e) {
      e.preventDefault()
      console.log(`${this.username} - ${this.password}`)
      this.login_credential = {
        username: this.username,
        password: this.password
      }
      axios.post('http://localhost:8001/api/token/', this.login_credential)
        .then((response) => {
          localStorage.feature_list = JSON.stringify(this.parseJwt(response.data.access).feature_list)
          this.$router.push('/dashboard')
        })
        .catch((err) => {
          this.errors.push(err)
        })
    },
  }
}
</script>


<style>
/* Sample `apply` at-rules with Tailwind CSS
.container {
  @apply min-h-screen flex justify-center items-center text-center mx-auto;
}
*/
.container {
  /* margin: 0 auto; */
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}

.input-form {
  border-bottom: solid 1px #aaa;
}
</style>
