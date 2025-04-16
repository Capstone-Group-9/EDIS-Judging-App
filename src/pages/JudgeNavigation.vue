<template>
  <q-page-container class="page-container">
    <q-page class="q-pa-none">
      <div>
        <h1>EDIS Teams</h1>
        <div v-if="teams.length > 0" class="teams-list">
          <div v-for="team in teams" :key="team.id" class="team-card">
            <div class="team-card-header">
              <div style="text-align: right">
                <h7>Team {{ team.id }}</h7>
              </div>
              <h2 style="margin: 0px; margin-top: 10px">{{ team.name }}</h2>
            </div>
            <div class="team-card-body">
              <p><strong>Members:</strong> {{ team.members.join(', ') }}</p>
              <p><strong>Score:</strong> {{ team.score }}</p>
            </div>
            <div style="display: flex; justify-content: right">
              <q-btn class="team-btn" label="Edit Team" flat no-caps />
              <q-btn class="team-btn" label="Remove Team" flat no-caps />
            </div>
          </div>
        </div>
        <div v-else class="text-center empty-notif q-mt-md">No teams available.</div>
      </div>
    </q-page>
  </q-page-container>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';

interface Team {
  id: number;
  name: string;
  members: string[];
  score: string;
}

export default {
  name: 'TeamList',
  setup() {
    const teams = ref<Team[]>([]);
    const getTeamData = async () => {
      try {
        const response = await fetch('http://localhost:5000/teamdata');
        if (!response.ok) {
          throw new Error(`error status: ${response.status}`);
        }
        const data = await response.json();
        teams.value = data;
      } catch (error) {
        console.error('Error retrieving team data:', error);
      }
    };

    onMounted(async () => {
      await getTeamData();
    });

    return {
      teams,
    };
  },
};
</script>

<style scoped>
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
  padding: 20px;
}
</style>
