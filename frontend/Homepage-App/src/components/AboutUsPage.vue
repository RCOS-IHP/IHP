<template>
  <div>
    <app-header></app-header>
    <div class="about-us">
      <div class="about-us-content container">
        <h1>About Us</h1>
        <p>
          IHP is a leading online education institute dedicated to providing top-quality courses for students around the world. Our mission is to empower individuals with the knowledge and skills they need to succeed in their careers and personal lives.
        </p>
        <img class="students-image" src="https://images.unsplash.com/photo-1598576065506-a1a50132daa8" alt="Group of students" />
      </div>
    </div>
    <ihp-footer></ihp-footer>
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import IhpFooter from "./components/IhpFooter.vue";

export default {
  name: "AboutUs",
  components: {
    AppHeader,
    IhpFooter,
  },
};
</script>

<style scoped>
.about-us {
  background-color: #ffffff;
  padding: 50px 0;
}

.about-us-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

.about-us-content h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

.about-us-content p {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 30px;
}

.students-image {
  width: 100%;
  max-height: 500px;
  object-fit: cover;
}
</style>