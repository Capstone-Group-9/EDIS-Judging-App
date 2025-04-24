<template>
  <q-page-container class="page-container">
    <q-page class="q-pa-none">
      <div class="main-container bg-image">
        <div class="content-container">
          <div>
            <div class="content-header">
              <span class="content-header-text">Add Team</span>
            </div>
          </div>
        </div>
      </div>
    </q-page>
  </q-page-container>
</template>

<style scoped>
.main-container {
  height: 100%;
}

h1 {
  font-size: 4rem;
  font-weight: bold;
  font: 'Kanit';
}

.empty-notif {
  font-size: 1.2rem;
  color: #949494;
}

.styled-btn {
  background-color: #bf2626;
  color: white;
  border-radius: 8px;
  padding: 10px 20px;
}
.styled-btn:hover {
  background-color: #9c0000;
  color: white;
}

.team-btn {
  background-color: #bf2626;
  color: white;
  border-radius: 8px;
  padding: 10px 20px;
  margin: 5px;
  margin-right: 0px;
}
.team-btn:hover {
  background-color: #9c0000;
  color: white;
}
.teams-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
  padding: 20px;
}
.team-card {
  border: 2px solid #bf2626;
  border-radius: 8px;
  background-color: #f9f9f9;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
.team-card:hover {
  transform: scale(1.02);
}
.team-card-header {
  font-size: 1.5rem;
  font-weight: bold;
  color: #bf2626;
  margin-bottom: 12px;
}
.team-card-body {
  font-size: 1rem;
  color: #333;
}
.page-container {
  height: 100vh;
  padding: 0px;
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
</style>
