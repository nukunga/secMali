<template>
   <q-page id="sub">
    <div id='wrap'>
      <div class="hero-banner">
        <div class="text-center preview-description fixed-top-center">
         <h1>SecMali</h1>
        </div>
       </div>
       <div class="flex flex-center">
    <q-splitter
      v-model="splitterModel"
      style="height: 500px; width: 90%;"
    >

      <template v-slot:before>
        <q-splitter
          v-model="insideModel"
          horizontal
        >

          <template v-slot:before>
            <q-scroll-area style="height: 100%;">
            <div class="q-pa-md">
              <div class="text-h4 q-mb-md">Before</div>
              <div v-for="n in 20" :key="n" class="q-my-md">{{ n }}. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</div>
            </div>
          </q-scroll-area>
          </template>

          <template v-slot:after>
            <q-scroll-area style="height: 100%;">
            <div class="q-pa-md">
              <div class="text-h4 q-mb-md">After</div>
              <div v-for="n in 20" :key="n" class="q-my-md">{{ n }}. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</div>
            </div>
            </q-scroll-area>
          </template>

        </q-splitter>
      </template>

      <template v-slot:after>
        <q-scroll-area style="height: 100%;">
        <div class="q-pa-md">
          <div class="text-h4 q-mb-md">Before</div>
          <div v-for="n in 20" :key="n" class="q-my-md">{{ n }}. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</div>
        </div>
        </q-scroll-area>
      </template>

    </q-splitter>
  </div> 
    </div>
   </q-page>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      splitterModel: ref(50), // start at 50%
      insideModel: ref(50)
    }
  }
}
</script>
<style scoped>
.sub {
  max-height: 100%;
}

.hero-banner {
  width: 98%;
    color: #131313;
    text-align: center;
    padding: 20px 0;
    font-weight: bold;
    margin-bottom: 20px;
}
.preview-description h1 {
    margin: 10px;
    -webkit-text-fill-color: #383F6D;
    -webkit-text-stroke: 3px #383F6D;
    font-size: 55px;
    font-family: 'Oxygen', sans-serif;
    text-transform: uppercase;
    letter-spacing: -4px;
}

body #wrap h1 {
  text-align: center;
  position: relative;
  width: 100%;
  line-height: 1.2;
  padding: 10px 0;
  color: #383F6D;
  font-weight: bold;
}


</style>
