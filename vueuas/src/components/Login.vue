<template>
  <div style="position: fixed; width: 100%; height: 100%; display: flex; justify-content: center;">
    <div style="position:absolute; width: 100%; height:100%; background: linear-gradient(110deg, #8EC5FC, #E0C3FC); z-index: -1;"></div>
    <div class="login-outer-container">
      <div class="login-container">
        <div class="login-inner-container">
          <div style="width: 100%; text-align: center; margin: 20px 0;">
            <h1 class="login-title" style="display: inline; font-size: 72px; color: #9599E2;">uas</h1>
          </div>
          <div style="display: flex; flex-direction: column; width: 100%; margin-top: 10px;">
            <label class="login-label">Username</label>
            <input class="login-input" ref="username" placeholder="mail address" spellcheck="false" @keypress="enterPassword"/>
          </div>
          <div style="display: flex; flex-direction: column; width: 100%; margin-top: 20px;">
            <label class="login-label">Password</label>
            <input class="login-input" ref="password" type="password" placeholder="password" spellcheck="false" @keypress="enterLogin"/>
          </div>
          <div style="width: 100%; text-align: right;">
            <div class="login-button" style="display: inline-block; margin-top: 30px; text-align: center; padding: 5px 15px;" @click="login">
              Login
            </div>
          </div>
          <br>
          <br>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Login",
  props: {
    navigateTo: { type: String, default: '/' },
  },
  methods: {
    enterLogin(e) {
      if (e.key === 'Enter') {
        this.login()
      }
    },
    enterPassword(e) {
      if (e.key === 'Enter') {
        this.$refs.password.select();
      }
    },
    login() {
      const username = this.$refs.username.value
      const password = this.$refs.password.value
      if (!/^([a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+@[a-zA-Z0-9_]+(.[a-zA-Z0-9_]+)+$/.test(username)) {
        alert(`Wrong format of mail address!`)
        return
      }
      axios.post('/login', {username, password}).then(response => {
        if (response.data.hasOwnProperty('token')) {
          const userToken = response.data.token
          document.cookie = `UserToken=${userToken}`
          location.assign(this.navigateTo)
        } else if (response.data.hasOwnProperty('error')) {
          alert(response.data.error)
        } else {
          alert(response.data)
        }
      })
    },
  }
}
</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  color: #555;
}

@media screen and (max-width: 480px) {
  .login-outer-container {
    width: 100%;
  }

  .login-container {
    width: calc(100% - 20px);
    background: white;
    padding: 20px 10px;
    margin-top: calc(15vh);
  }

  .login-inner-container {
    width: 100%;
  }
}

@media screen and (min-width: 480px) {
  .login-outer-container {

  }

  .login-container {
    width: 300px; background: white; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,.3); padding: 10px; margin-top: calc(15vh);
  }

  .login-inner-container {
    width: 90%; margin-left: 5%; margin-right: 5%;
  }
}


.login-title {
  background: linear-gradient(110deg, #8EC5FC, #E0C3FC);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

.login-label {
  width: 100%;
  margin-bottom: 5px;
  font-size: 18px;
}

.login-input {
  width: calc(100% - 30px);
  outline: none;
  border-radius: 4px;
  height: 32px;
  border: 1px solid #ddd;
  padding-left: 15px;
  padding-right: 15px;
  font-size: 16px;
  background: rgba(255,255,255,0);
}

.login-input:active {

}

.login-button {
  color: #555;
  border: 1px solid #555;
  border-radius: 4px;
  cursor: pointer;
}

.login-button:hover {
  background: #555;
  color: white;
}

</style>