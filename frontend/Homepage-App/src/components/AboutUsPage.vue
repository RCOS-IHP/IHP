<template>
  <div>
    <AppHeader />
    <div class="about-us">
      <div class="about-us-content container">
        <h1>About Us</h1>
        <p>
          IHP is a leading online education institute dedicated to providing top-quality courses for students around the world. Our mission is to empower individuals with the knowledge and skills they need to succeed in their careers and personal lives.
        </p>
        <img class="students-image" src="https://images.unsplash.com/photo-1598576065506-a1a50132daa8" alt="Group of students" />
      </div>
      <div class="timeline-container container">
        <h2>Our Milestones</h2>
        <ul class="timeline">
          <li>
            <span>2015</span> - IHP was founded
          </li>
          <li>
            <span>2016</span> - First online course released
          </li>
          <li>
            <span>2017</span> - Reached 10,000 students
          </li>
          <li>
            <span>2018</span> - Expanded to new subject areas
          </li>
          <li>
            <span>2019</span> - Launched mobile app
          </li>
          <li>
            <span>2020</span> - Partnered with leading universities
          </li>
        </ul>
        <h2>Core Values</h2>
        <ul class="core-values">
          <li>Quality Education</li>
          <li>Accessibility</li>
          <li>Innovation</li>
          <li>Collaboration</li>
          <li>Commitment to Excellence</li>
        </ul>
      </div>
    </div>
    <IhpFooter />
  </div>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";
import IhpFooter from "@/components/IhpFooter.vue";

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

.timeline-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
  padding-bottom: 50px;
}

.timeline-container h2 {
  font-size: 30px;
  margin: 40px 0;
}

.timeline {
  list-style-type: none;
  padding: 0;
}

.timeline li {
  font-size: 18px;
  margin: 10px 0;
}

.timeline li span {
  font-weight: bold;
  margin-right: 10px;
}

.core-values {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.core-values li {
  font-size: 18px;
  padding: 10px;
  border: 1px solid #595FD9;
  border-radius: 4px;
  margin-bottom: 10px;
  width: calc(33% - 10px);
  text-align: center;
}
</style>