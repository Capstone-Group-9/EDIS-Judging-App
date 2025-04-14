<template>
  <q-table :rows="leaderboard" :columns="columns" row-key="id" />
</template>

<script lang="ts">
export default {
  data() {
    return {
      leaderboard: [
        { id: 1, name: 'Konveyor', score: 1 },
        { id: 2, name: 'team 2', score: 2 },
        { id: 3, name: 'team 3', score: 3 },
      ] as { id: number; name: string; score: number }[],

      columns: [
        { name: 'number', label: 'Team Number', field: 'id' },
        { name: 'name', label: 'Team Name', field: 'name' },
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
