<template>
  <footer class="ihp-footer">
    <div class="container">
      <div class="social-media">
        <h4>Connect with us</h4>
        <ul>
          <li><a href="#" target="_blank" rel="noopener noreferrer"><font-awesome-icon :icon="['fab', 'facebook-f']" /></a></li>
          <li><a href="#" target="_blank" rel="noopener noreferrer"><font-awesome-icon :icon="['fab', 'twitter']" /></a></li>
          <li><a href="#" target="_blank" rel="noopener noreferrer"><font-awesome-icon :icon="['fab', 'linkedin-in']" /></a></li>
          <li><a href="#" target="_blank" rel="noopener noreferrer"><font-awesome-icon :icon="['fab', 'youtube']" /></a></li>
        </ul>
      </div>
      <div class="footer-sections">
        <div class="footer-section">
          <h4>About IHP</h4>
          <ul>
            <li><a href="#">Company Information</a></li>
            <li><a href="#">Featured Products</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">News and Events</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Customer Support</h4>
          <ul>
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">Support Services</a></li>
            <li><a href="#">FAQs</a></li>
            <li><a href="#">Accessibility</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Legal</h4>
          <ul>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Cookie Policy</a></li>
            <li><a href="#">Terms of Use</a></li>
            <li><a href="#">Permissions</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2023 IHP. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'IhpFooter',
};
</script>

<style scoped>
.ihp-footer {
  background-color: #f8f8f8;
  padding: 30px 0;
  font-family: Arial, sans-serif;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

.social-media {
  margin-bottom: 20px;
}

.social-media h4 {
  font-size: 18px;
  margin-bottom: 15px;
}

.social-media ul {
  list-style: none;
  display: flex;
  padding: 0;
}

.social-media li {
  margin-right: 10px;
}

.social-media a {
  text-decoration: none;
  color: #333;
  font-size: 24px;
}

.social-media a:hover {
  color: #666;
}

.footer-sections {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
}

.footer-section {
  width: calc(100% / 3 - 20px);
}

<style scoped>
/* ...previous CSS styles */

.footer-section h4 {
  font-size: 18px;
  margin-bottom: 15px;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section li {
  margin-bottom: 10px;
}

.footer-section a {
  text-decoration: none;
  color: #333;
}

.footer-section a:hover {
  color: #666;
}

.footer-bottom {
  text-align: center;
  font-size: 14px;
  color: #666;
}

@media (max-width: 768px) {
  .social-media {
    text-align: center;
    margin-bottom: 30px;
  }

  .footer-sections {
    flex-direction: column;
  }

  .footer-section {
    width: 100%;
    margin-bottom: 30px;
  }

  .footer-section:last-child {
    margin-bottom: 0;
  }
}
</style>
