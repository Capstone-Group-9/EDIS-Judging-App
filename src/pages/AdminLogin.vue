<template>
  <q-page-container>
    <q-page>
      <div class="main-container">
        <div class="content-header">
          <span class="content-header-text">ADMINISTRATOR LOGIN</span>
        </div>
      </div>

      <div class="row justify-center q-pt-md">
        <div class="q-pa-md" style="width: 100%; max-width: 400px">
          <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
            <q-input filled label="Username" />

            <q-input filled label="Password" type="password" />

            <div class="row justify-center q-mt-md">
              <q-btn label="Submit" type="submit" class="styled-btn" to="/admin-dashboard" flat />
            </div>
          </q-form>
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

.content-header-text {
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  color: white;
  letter-spacing: 1px;
  padding-left: 10px;
}

.styled-btn {
  background-color: #bf2626;
  color: white;
  border-radius: 8px;
  padding: 10px 20px;
}
</style>
