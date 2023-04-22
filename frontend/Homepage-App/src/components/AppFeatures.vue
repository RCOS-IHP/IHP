<template>
  <section class="app-features">
    <div class="features-container">
      <h2 class="section-title">Our Features</h2>
      <div class="features">
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
  background-color: #f0f2f9;
}

.features-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.section-title {
  font-size: 36px;
  font-weight: bold;
  color: #595FD9;
  margin-bottom: 40px;
}

.features {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.feature {
  position: relative;
  width: calc(33% - 40px);
  background-color: #ffffff;
  padding: 20px;
  border: 2px solid #595FD9;
  border-radius: 4px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.feature:hover {
  transform: translateY(-10px);
}

.feature-image {
  width: 100%;
  height: 400px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  filter: brightness(60%);
  margin-bottom: 20px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

.feature h3 {
  font-size: 28px;
  margin-bottom: 10px;
  color: #595FD9;
}

.feature p {
  font-size: 18px;
}
</style>