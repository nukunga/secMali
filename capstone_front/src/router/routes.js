
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/UploadPage.vue') },
      { path: 'result', component: () => import('pages/ResultPage.vue') },
      { path: 'test', component: () => import('pages/TestPage.vue') },
      { path: 'loading', component: () => import('pages/LoadingPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
