<template>
  <q-page-container>
    <q-page class="q-pa-none">
      <div class="q-pa-md q-gutter-sm">
        <q-btn class="styled-btn" label="Add/Update Team Information" flat no-caps />
      </div>
    </q-page>
  </q-page-container>
</template>

<script setup lang="ts"></script>

<style scoped>
.styled-btn {
  font-family: 'Inter';
  font-weight: bold;
  border: 1px solid #d3d6db;
  background-color: transparent;
  color: #000;
  padding: 10px 20px;
}

.styled-btn:hover {
  border-color: #a0a4a8;
  color: #333;
}
</style>
