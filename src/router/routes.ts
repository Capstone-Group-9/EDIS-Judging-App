import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'admin', component: () => import('pages/AdminNavigation.vue') },
    ],
  },
   {
     path: '/judge',
     component: () => import('layouts/MainLayout.vue'),
     children: [
      { path: '', component: () => import('pages/JudgeDashboard.vue') },
      { path: 'vote', component: () => import('pages/JudgeVote.vue') }
    ],
   },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
