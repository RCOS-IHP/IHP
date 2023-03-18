<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-logo">
        <span style="color: #595FD9;">IHP</span>
      </div>
      <div class="footer-links">
        <a href="#">Terms</a>
        <a href="#">Privacy</a>
        <a href="#">Support</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "AppFooter",
};
</script>

<style scoped>
.app-footer {
  background-color: white;
  padding: 20px 0;
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-logo {
  font-size: 24px;
  font-weight: bold;
}

.footer-links a {
  color: #595FD9;
  margin-left: 20px;
  text-decoration: none;
}

.footer-links a:hover {
  text-decoration: underline;
}
</style>
