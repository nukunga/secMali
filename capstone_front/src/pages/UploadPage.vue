<template>
  <q-page class="q-pa-xl" id="main">
    <div id='wrap'>
  <h1>SecMali</h1>
  <div class='panel'>
    <div class="h2">
    <h2 class='dark' data-splitting='words'>Document <br>Analysis</h2>
    </div>
    <div class='file' style="max-width: 400px;">
      <q-file filled bottom-slots v-model="model" label="Upload File" counter>
        <template v-slot:prepend>
          <q-icon name="cloud_upload" @click.stop.prevent />
        </template>
        <template v-slot:append>
          <q-icon name="close" @click.stop.prevent="model = null" class="cursor-pointer" />
        </template>
      </q-file>
    </div>
  </div>
</div>

<section class="">
    <div class="container">
        <div class="col-7 details">
            <h3>문서 열람 전 꼭 확인하세요!</h3>
            <p>최근 몇 년간 악성 문서를 통한 피싱 범죄 비율이 기하급수적으로 늘고 있습니다. <br>문서 열람 전 미리 확인하여 문서에 어떤 매크로 코드가 포함되어 있는지 확인해보세요.</p>
        </div>
    </div>
</section>

<section class="section--primary">
    <div class="container">
        <div class="col-3 features">
            <i class="fa fa-bolt"></i>
            <p>
              <q-img src="~assets\secure.png" width="128px" id="pimg"></q-img><br><br><br>
                악성 매크로 코드 분석 결과<br> 제공을 통한 보안 의식 강화
            </p>
        </div>
        <div class="col-3 features">
            <i class="fa fa-bank"></i>
            <p>
              <q-img src="~assets\order.png" width="150px"></q-img><br><br>
                악성 매크로 코드가 <br>지시하는 명령을 자세하게 제공
            </p>
        </div>
        <div class="col-3 features">
            <i class="fa fa-heart"></i>
            <p>
              <q-img src="~assets\analysis.png" width="147px"></q-img><br><br>
                비전공자도 입문하기 쉬운 형태로 <br>분석 자료 제공
            </p>
        </div>
    </div>
</section>

<section class="section--primary--alt">
    <div class="container">
        <h3>Test the safety of documents anytime, anywhere through the SecMali.</h3>
        <p>Be sure to check the document before viewing it! We are no longer free from phishing attacks. <br>In recent years, the rate of phishing crimes through malicious documents has increased exponentially. <br>Check before viewing the document to see what macro code the document contains.</p>
    </div>
</section>
  </q-page>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      model: ref(null)
    }
  }
}
</script>

<style scoped>
#q-pa-xl {
  width: 100%;
}
* {
    box-sizing: border-box;
}

html {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}

body {
  scroll-behavior: smooth;
  background: white;
  font-family: "Lexend Mega", sans-serif;
  pointer-events: none;
  max-width: 100%;
  box-sizing: border-box;
  margin: 0 auto;
  padding: 0;
}

/*본문 구조*/
body #wrap {
  width: 1000px;
  max-width: 85vw;
  margin: 0px auto;
  padding: 50px;
  position: relative;
  box-sizing: border-box;
}
/*본문 구조*/

/*secmali*/
body #wrap h1 {
  text-align: center;
  font-family: "Bogart-Semibold";
  font-size: 100px;
  position: relative;
  width: 100%;
  line-height: 1.2;
  padding: 10px 0;
  overflow: hidden;
  margin-bottom: 10px;
  color: #383F6D;
  font-weight: bold;
}
/*secmali*/

/*secmali 밑 줄*/
body #wrap h1:before, body #wrap h1:after {
  content: "";
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: 0;
  left: 0;
  background: #383F6D;
  z-index: 2;
}
/*secmali 밑 줄*/

/*본문내용*/
body #wrap .panel {
  position: relative;
  width: 100%;
  margin-bottom: 25vh;
  max-height: 40vh;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  padding: 20px;
  box-sizing: border-box;
}

/*Document Analysis*/
body #wrap .panel h2 {
  font-family: "Bogart-Semibold";
  font-size: 64px;
  position: relative;
  z-index: 3;
  color: #300264;
  line-height: 1;
  pointer-events: none;
  font-weight: bold;
}

@media (min-width: 1000px) {
  body #wrap .panel h2 {
    grid-area: 3/1/4/5;
    font-size: 82px;
  }
}

/*Document Analysis*/
body #wrap .panel .file {
  grid-area: 2/3/5/6;
  position: relative;
}

a {
    text-decoration: none;
}
a:hover {
    text-decoration: none;
}

img {
    max-width: 100%;
}
.container {
    margin: 0 auto;
    width: 100%;
    text-align: center;
}

header h1 {
    font-size: 3rem;
    margin: 0 0 1rem;
}
@media (max-width: 43.75em) {
    header h1 {
        font-size: 2rem;
    }
}
header h2 {
    font-weight: 300;
    font-size: 1.5rem;
    margin: 0 0 1rem;
}
@media (max-width: 43.75em) {
    header h2 {
        font-size: 1.5rem;
    }
}

section {
    background: #3B527C;
    color: white;
    padding: 3.5rem 0;
}
@media (max-width: 43.75em) {
    section {
        padding: 2rem 0;
    }
}
section.section--primary {
    background: #E2F0FF;
    color: black;
}
section.section--primary--alt {
    background: white;
    color: black;
}

section h3 {
    text-align: center;
    font-size: 2rem;
    font-weight: 500;
    margin: 0 0 1rem;
}

@media (max-width: 43.75em) {
    section h3 {
        font-size: 1.5rem;
    }
}
section li {
    font-size: 1.2rem;
    font-weight: 300;
}
section p {
    font-size: 1.2rem;
    font-weight: 300;
}

.col, .col-5, .col-3, .col-7 {
    margin: 0 1.5%;
    display: inline-block;
    vertical-align: top;
}

.col-7 {
    width: 64%;
}
@media (max-width: 43.75em) {
    .col-7 {
        width: 100%;
        margin: 0;
        text-align: center;
    }
}

.col-3 {
    width: 29%;
}
@media (max-width: 43.75em) {
    .col-3 {
        width: 100%;
        margin: 0;
    }
}

.col-5 {
    width: 30%;
}
@media (max-width: 34.375em) {
    .col-5 {
        width: 60%;
        margin: 0;
    }
}

.details {
    text-align: center;
}
.details h3 {
    font-size: 2rem;
    text-align: center;
}


.features {
    text-align: center;
    padding: 1rem;
}

.features p {
    margin: 0 0 1rem 0;
    font-size: 1rem;
    font-weight: 700;
}

.text--center {
    text-align: center;
}

.text--left {
    text-align: left;
}
</style>