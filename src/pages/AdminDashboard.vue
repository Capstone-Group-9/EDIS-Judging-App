<template>
  <q-page-container>
    <q-page>
      <div class="main-container">
        <div class="content-header">
          <span class="content-header-text">ADMIN</span>
        </div>
      </div>

      <div class="row justify-center q-pt-lg">
        <div class="q-pa-lg" style="width: 100%; max-width: 700px">
          <q-item
            clickable
            v-ripple
            class="q-mb-md bordered-item"
            tag="router-link"
            to="/admin-teams"
            q-py-lg
          >
            <q-item-section avatar>
              <q-icon name="group" />
            </q-item-section>

            <q-item-section> Edit Team Information </q-item-section>

            <q-item-section side>
              <q-icon name="chevron_right" />
            </q-item-section>
          </q-item>

          <q-item clickable v-ripple class="q-mb-md bordered-item" q-py-lg>
            <q-item-section avatar>
              <q-icon name="emoji_events" />
            </q-item-section>

            <q-item-section> Update Judge Information </q-item-section>

            <q-item-section side>
              <q-icon name="chevron_right" />
            </q-item-section>
          </q-item>

          <q-item clickable v-ripple class="bordered-item" q-py-lg>
            <q-item-section avatar>
              <q-icon name="event" />
            </q-item-section>

            <q-item-section> Edit Event Information </q-item-section>

            <q-item-section side>
              <q-icon name="chevron_right" />
            </q-item-section>
          </q-item>
        </div>
      </div>
    </q-page>
  </q-page-container>
</template>

<script lang="ts"></script>

<style scoped>
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

.bordered-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 12px;
  background-color: white;
}

.content-header-text {
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  color: white;
  letter-spacing: 1px;
  padding-left: 10px;
}

.styled-btn {
  background-color: clear;
  color: black;
  border-radius: 8px;
  padding: 10px 20px;
  border: 1px solid gray;
  border-radius: 8px;
}
</style>
