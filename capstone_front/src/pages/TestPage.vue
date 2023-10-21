<template>
  <q-page class="column justify-center content-center items-center q-gutter-sm">
    <div class="fixed-top text-h6 text-uppercase text-center q-pa-sm">test page</div>

    <q-card class="bg-grey-5" v-for="item in res" :key="item">
      <q-card-section class="text-subtitle1 text-bold text-red">{{ item.name }}</q-card-section>
      <q-card-section>document id is <span class="text-blue">{{ item.testDocId }}</span></q-card-section>
      <q-card-section>document content is <span class="text-white">{{ item.content }}</span></q-card-section>
    </q-card>
  </q-page>
</template>

 <script>
 import { defineComponent, onMounted, ref } from 'vue'
 import { testFunction } from 'src/services/test';

 export default defineComponent({
   name: 'TestPage',
   setup() {
    const res = ref([]);

    onMounted(() => {
      res.value = testFunction();
    })

    return{
      res
    }
   }
 })
 </script>
