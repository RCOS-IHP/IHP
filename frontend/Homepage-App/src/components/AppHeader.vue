<template>
  <header class="app-header">
    <nav>
      <a href="#" class="logo">
        <span style="color: #595FD9;">IHP</span>
      </a>
      <div class="menu-items">
        <a href="#">Courses</a>
        <a href="#">Pricing</a>
        <a href="#">Resources</a>
        <a href="#">Contact</a>
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

.menu-items a {
  color: #595FD9;
  margin-left: 20px;
  text-decoration: none;
}

.menu-items a:hover {
  text-decoration: underline;
}
</style>
