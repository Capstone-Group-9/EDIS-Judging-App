<template>
  <q-page-container class="page-container">
    <q-page class="q-pa-none">
      <div class="main-container bg-image">
        <div class="content-container">
          <div class="content-header">
            <span class="content-header-text">Edit Team {{ teamId }}</span>
          </div>

          <div v-if="teaminfo" class="q-pa-lg">
            <q-form @submit.prevent="submitchanges" class="edit-form">
              <q-input filled v-model="teaminfo.name" label="Team Name" class="q-mb-md" required />
              <q-input
                filled
                v-model="teaminfo.teamcategory"
                label="Team Category"
                class="q-mb-md"
                required
              />
              <q-input
                filled
                v-model.number="teaminfo.totalscore"
                type="number"
                label="Total Score"
                class="q-mb-md"
                required
              />

              <div class="q-mt-md">
                <q-btn label="Save Changes" type="submit" class="styled-btn" />
              </div>
            </q-form>
          </div>
          <div v-else class="q-pa-md flex flex-center">
            <q-spinner-dots color="primary" size="40px" />
          </div>
        </div>
      </div>
    </q-page>
  </q-page-container>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

interface Team {
  id: number;
  name: string;
  teamcategory: string;
  totalscore: number;
  scores: number[];
}

export default {
  name: 'EditTeamPage',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const teamId = ref<number | null>(null);
    const teaminfo = ref<Team | null>(null);
    const scoreinput = ref<string>('');

    const rawTeamId = route.params.id as string;
    teamId.value = parseInt(rawTeamId, 10);

    onMounted(async () => {
      if (teamId.value === null) {
        console.error('Invalid team ID');
        await router.push('/error');
        return;
      }

      const response = await fetch(`http://localhost:5000/teams`);
      if (!response.ok) throw new Error('Could not fetch team data');

      const teams: Team[] = await response.json();

      let targetTeam = null;

      for (let i = 0; i < teams.length; i++) {
        if (teams[i].id === teamId.value) {
          targetTeam = teams[i];
          break;
        }
      }

      if (!targetTeam) throw new Error('Team not found');

      teaminfo.value = targetTeam;
    });

    const submitchanges = async () => {
      if (!teaminfo.value || teamId.value === null) {
        await router.push('/ErrorNotFound');
      }

      try {
        const response = await fetch(`http://localhost:5000/teams/${teamId.value}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(teaminfo.value),
        });

        if (!response.ok) {
          throw new Error('Could not update team');
        }
        await router.push('/admin');
      } catch {
        await router.push('/ErrorNotFound');
      }
    };

    return {
      teamId,
      teaminfo,
      scoreinput,
      submitchanges,
    };
  },
};
</script>

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
