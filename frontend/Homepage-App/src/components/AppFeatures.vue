<template>
  <section class="app-features">
    <div class="features-container">
      <div class="feature">
        <div class="feature-image" style="background-image: url('https://source.unsplash.com/random?education');"></div>
        <h3>High-Quality Courses</h3>
        <p>Learn from industry-leading experts and unlock new opportunities</p>
      </div>
      <div class="feature">
        <div class="feature-image" style="background-image: url('https://source.unsplash.com/random?college-students-studying');"></div>
        <h3>Flexible Learning</h3>
        <p>Study at your own pace with access to courses anytime, anywhere</p>
      </div>
      <div class="feature">
        <div class="feature-image" style="background-image: url('https://source.unsplash.com/random?affordable-education');"></div>
        <h3>Affordable Education</h3>
        <p>Unlock the power of education without breaking the bank</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AppFeatures",
};
</script>

<style scoped>
.app-features {
  padding: 60px 0;
  background-color: #DFE2E0;
}

.features-container {
  max-width: 1200px;
  margin: 0 auto;
}

.feature {
  position: relative;
  text-align: center;
  margin-bottom: 60px;
}

.feature-image {
  width: 100%;
  height: 300px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  filter: brightness(60%);
  margin-bottom: 20px;
}

.feature h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

.feature p {
  font-size: 16px;
}
</style>
