<template>
  <q-page-container>
    <q-page class="q-pa-none">
      <div class="main-container bg-image">
        <div class="content-header">
          <span class="content-header-text">TEAM NAME</span>
        </div>
        <div class="image-column">
          <q-img
            src="~assets/placeholderTeam.svg"
            alt="Speed School Logo"
            class="school-image"
            :width="'350px'"
            :height="'250px'"
          />
        </div>
      </div>
    </q-page>
  </q-page-container>
</template>

<script setup lang="ts"></script>

<style scoped>
.main-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.bg-image {
  background-image: url('src/assets/gray-background.png');
  background-repeat: no-repeat;
  background-size: cover;
}

.content-row {
  display: flex;
  gap: 40px;
}

.text-column {
  flex: 1;
}

.text-column p {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  margin-bottom: 20px;
}

.image-column {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-header {
  display: inline-block;
  padding: 10px 100px;
  background-color: #bf2626;
  clip-path: polygon(0 0, 90% 0, 100% 100%, 0% 100%);
  margin-left: 0;
  color: white;
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  letter-spacing: 1px;
}

.content-header-text {
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  color: white;
  letter-spacing: 1px;
  padding-left: 10px;
}

.carousel-container {
  width: 80%;
  margin: 0 auto;
  padding: 0 15px;
}

@media (max-width: 768px) {
  .content-row {
    flex-direction: column;
  }

  .image-column {
    order: -1;
    margin-bottom: 30px;
  }
}
</style>
