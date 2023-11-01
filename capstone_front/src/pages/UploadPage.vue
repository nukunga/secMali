<template>
  <q-page id="main">
    <div id='wrap'>
        <div class="hero-banner">
    <div class="text-center preview-description">
        <h1>SecMali</h1>
			<small style="font-style: oblique">Document Analysis Program</small>
    </div>
</div>
     <div class="flex flex-center">
        <q-uploader
        url="http://localhost:4444/upload"
        color="indigo-9"
        accept=".hwp, .doc, .xlsx"
        flat
        bordered
        style="width: 600px; margin-top:150px; margin-bottom:150px"
      />
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

.hero-banner {
    color: #131313;
    text-align: center;
    padding: 50px 0;
    font-weight: bold;
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
  width: 100%;
  margin: 0;
}

/*secmali*/
body #wrap h1 {
  text-align: center;
  font-size: 100px;
  position: relative;
  width: 100%;
  line-height: 1.2;
  padding: 10px 0;
  overflow: hidden;
  margin-bottom: 20px;
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

/*밑에 본문 가운데 정렬*/
.container {
    margin: 0;
    width: 100%;
    text-align: center;
}
/*밑에 본문 가운데 정렬*/

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
    font-weight: 700;
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