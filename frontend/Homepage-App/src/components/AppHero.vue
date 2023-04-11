<template>
  <section class="app-hero">
    <div class="hero-content">
      <h1>Welcome to IHP</h1>
      <p>Unlock the power of education with our high-quality courses and flexible learning options</p>
      <a href="#" class="cta-button">Explore Courses</a>
    </div>
  </section>
</template>

<script>
export default {
  name: "AppHero",
};
</script>

<style scoped>
.app-hero {
  position: relative;
  height: 60vh;
  background: linear-gradient(
      125deg,
      rgba(89, 95, 217, 0.6) 0%,
      rgba(223, 226, 224, 0.6) 100%
    ),
    url('https://source.unsplash.com/random?education');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: white;
}

.hero-content h1 {
  font-size: 48px;
  margin-bottom: 20px;
}

.hero-content p {
  font-size: 24px;
  margin-bottom: 40px;
}

.cta-button {
  display: inline-block;
  background-color: #595FD9;
  color: white;
  padding: 10px 20px;
  font-size: 18px;
  text-decoration: none;
  border-radius: 4px;
}

.cta-button:hover {
  background-color: #4d52d6;
}
</style>

