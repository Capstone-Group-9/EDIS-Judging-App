<template>
  <q-table :rows="teams" :columns="columns" row-key="id" />
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
      columns: [
        { name: 'number', label: 'Team Number', field: 'id' },
        { name: 'name', label: 'Team Name', field: 'name' },
        { name: 'members', label: 'Team Memebers', field: 'members' },
        { name: 'score', label: 'Score', field: 'score' },
      ] as { name: string; label: string; field: string }[],
      pagination: {
        rowsPerPage: 10,
        page: 1,
      } as { rowsPerPage: number; page: number },
    };
  },
};
</script>

<style scoped>
.q-page {
  padding: 20px;
}

.q-table {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  font-size: 24px;
  font-weight: bold;
}
</style>
