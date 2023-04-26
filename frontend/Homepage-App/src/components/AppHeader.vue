<template>
  <header class="app-header">
    <nav>
      <a href="#" class="logo">
        <span style="color: #595FD9;">IHP</span>
      </a>
      <div class="menu-items">
        <a href="#">Courses</a>
        <a href="#">Pricing</a>
        <router-link to="/aboutus">AboutUs</router-link>
      </div>
      <div class="buttons">
        <button class="login-btn">Login</button>
        <button class="signup-btn">Sign Up</button>
      </div>
    </nav>
  </header>
</template>
<script>
export default {
  name: "AppHeader",
};
</script>
<style scoped>
@keyframes hover {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}

.app-header {
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

.logo:hover {
  animation: hover 2s infinite;
}

.menu-items a,
.router-link-exact-active {
  color: #595FD9;
  margin-left: 20px;
  text-decoration: none;
  transition: color 0.3s;
}

.menu-items a:hover,
.router-link-exact-active:hover {
  text-decoration: underline;
  color: #3a3fd5;
  animation: hover 2s infinite;
}

.buttons {
  display: flex;
}

.login-btn,
.signup-btn {
  background-color: #595FD9;
  color: #ffffff;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  margin-left: 10px;
  cursor: pointer;
  outline: none;
  transition: background-color 0.3s;
}

.login-btn:hover,
.signup-btn:hover {
  background-color: #3a3fd5;
  animation: hover 2s infinite;
}
</style>
