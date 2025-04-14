<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="header">
      <q-toolbar class="header-toolbar">
        <q-toolbar-title class="header-title"> EDIS </q-toolbar-title>

        <div class="header-links-container">
          <EssentialLink
            class="header-links"
            v-for="link in linksList"
            :key="link.title"
            v-bind="link"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container class="q-pa-none">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import EssentialLink, { type EssentialLinkProps } from 'components/EssentialLink.vue';

const linksList: EssentialLinkProps[] = [
  {
    title: 'Home',
    link: '/',
  },
  {
    title: 'Administrators',
    link: '/admin',
  },
  {
    title: 'Judges',
    link: '/judging',
  },
];
</script>

<style scoped>
.header {
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  background-color: #bf2626;
}

.header-toolbar {
  display: flex;
  align-items: center;
  width: 100%;
}

.header-title {
  font-family: 'Kanit', sans-serif;
  font-size: 36px;
  font-weight: 800;
  color: white;
  letter-spacing: 1px;
}

.header-links-container {
  display: flex;
  align-items: center;
}

.header-links {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 500;
  color: white;
  letter-spacing: 0.4px;
  margin-left: 15px;
  text-decoration: none;
}
</style>
