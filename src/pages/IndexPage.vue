<template>
  <q-page-container>
    <q-page class="q-pa-none">
      <div class="main-container">
        <h2 class="section-title">ENGINEERING DESIGN & INNOVATION SHOWCASE</h2>
        <div class="divider-line"></div>

        <div class="content-row">
          <div class="text-column">
            <p>
              The Engineering Design & Innovation Showcase (EDIS) is a signature event at the J.B.
              Speed School of Engineering that highlights the creativity, collaboration, and
              technical expertise of our senior engineering students. Held at the end of each
              semester, the showcase features capstone design projects developed in partnership with
              industry sponsors and community partners.
            </p>
            <p>
              Students work in interdisciplinary teams to solve real-world problems, applying the
              skills they've gained throughout their academic careers. Projects span all major
              engineering disciplines and are judged by industry professionals and faculty based on
              innovation, design, functionality, and impact.
            </p>
          </div>
          <div class="image-column">
            <q-img
              src="~assets/speed-school.png"
              alt="Speed School Logo"
              class="school-image"
              :width="'350px'"
              :height="'250px'"
            />
          </div>
        </div>

        <div class="content-header">
          <span class="content-header-text">LIVE RESULTS</span>
        </div>

        <div class="content-row">
          <div class="q-pa-md leaderboard">
            <q-list bordered padding>
              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 1</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 2</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 3</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 4</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 5</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>
            </q-list>
          </div>
          <div class="q-pa-md leaderboard">
            <q-list bordered padding>
              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 6</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 7</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 8</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>
              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 9</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>

              <q-separator spaced inset="item" />

              <q-item>
                <q-item-section top avatar>
                  <q-avatar color="red" text-color="white" icon="person" />
                </q-item-section>

                <q-item-section>
                  <q-item-label>Team 10</q-item-label>
                  <q-item-label caption lines="2"
                    >Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit
                    elit.</q-item-label
                  >
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>

        <div class="content-header-flip">
          <span class="content-header-text">TEAMS</span>
        </div>

        <div class="content-row full-width q-pt-lg">
          <div class="carousel-container">
            <q-carousel
              arrows
              animated
              v-model="currentSlide"
              height="400px"
              class="rounded-borders"
            >
              <q-carousel-slide name="first" img-src="src/assets/GROUP SAMPLE 2.jpg">
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2 text-white">Team 1</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide name="second" img-src="src/assets/GROUP SAMPLE 1.jpg">
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2 text-white">Team 2</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide name="third" img-src="src/assets/GROUP SAMPLE 3.jpg">
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2 text-white">Team 3</div>
                </div>
              </q-carousel-slide>
            </q-carousel>
          </div>
        </div>
      </div>
    </q-page>
  </q-page-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const currentSlide = ref('first');
</script>

<style scoped>
.main-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.section-title {
  font-family: 'Inter', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: #333;
  text-align: center;
  margin-bottom: 10px;
}

.divider-line {
  height: 3px;
  width: 100px;
  background-color: #bf2626;
  margin: 0 auto 30px;
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

.content-header-flip {
  display: inline-block;
  padding: 10px 40px;
  background-color: #bf2626;
  clip-path: polygon(10% 0, 100% 0, 100% 100%, 0 100%);
  margin-left: auto;
  margin-right: 0;
  float: right;
  color: white;
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  letter-spacing: 1px;
  text-align: right;
}
.content-header-text {
  font-family: 'Kanit', sans-serif;
  font-size: 30px;
  font-weight: 800;
  color: white;
  letter-spacing: 1px;
  padding-left: 10px;
}

.school-image {
  object-fit: contain;
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

.leaderboard {
  max-width: 500px;
}
</style>
