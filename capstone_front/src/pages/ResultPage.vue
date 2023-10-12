<template>
   <q-page id="sub">
    <div>
    <p style="text-align: center">
    <img id="subname" width="200" draggable="false" src="~assets\secmali_name.png">
    </p>
  </div>
  <div>
    <div class="pie-chart pie-chart1" id="pie"><span class="center">100%</span></div>
    <textarea id="one" style="resize: none;">파일명 :&#10;파일 확장자 : </textarea>
  </div>
  <div class="tabmenu out-tabmenu" id="menu">
    <ul>
      <li id="tab1" class="btnCon">
        <input type="radio" checked name="tabmenu" id="tabmenu1">
        <label for="tabmenu1">악성코드</label>
        <div class="tabCon" >

          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.v



        </div>

      </li>
      <li id="tab2" class="btnCon"><input type="radio" name="tabmenu" id="tabmenu2">
        <label for="tabmenu2">코드분석</label>
        <div class="tabCon" >It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</div>

      </li>
    </ul>
  </div>
   </q-page>
</template>
  
  <script>
  import { defineComponent } from 'vue'
  
  export default defineComponent({
    name: 'ErrorNotFound'
  })
  </script>
<style scoped>
#sub {
  background-color: #F7F8FF;
}

#subname {
  margin-top: 50px;
  text-align: center;
}

.pie-chart {
  position: relative;
  display:inline-block;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  transition: 0.3s;
  margin-left: 100px;
  margin-top: 50px;
}

span.center{
  background: #fff;
  display : block;
  position: absolute;
  top:50%; left:50%;
  width:100px; height:100px;
  border-radius: 50%;
  text-align:center;
  line-height: 100px;
  font-size:25px;
  color: #000;
  transform: translate(-50%, -50%);
}

.pie-chart1{
  animation: pie1 0.5s forwards;
}

@keyframes pie1{
  0%{background : conic-gradient(#bbbee6 0% 0%, #ffffff 0% 100%)}
  5%{background : conic-gradient(#bbbee6 0% 5%, #ffffff 0% 100%)}
  10%{background : conic-gradient(#bbbee6 0% 10%, #ffffff 0% 100%)}
  15%{background : conic-gradient(#bbbee6 0% 15%, #ffffff 0% 100%)}
  20%{background : conic-gradient(#bbbee6 0% 20%, #ffffff 0% 100%)}
  25%{background : conic-gradient(#bbbee6 0% 25%, #ffffff 0% 100%)}
  30%{background : conic-gradient(#bbbee6 0% 30%, #ffffff 0% 100%)}
  35%{background : conic-gradient(#bbbee6 0% 35%, #ffffff 0% 100%)}
  40%{background : conic-gradient(#bbbee6 0% 40%, #ffffff 0% 100%)}
  45%{background : conic-gradient(#bbbee6 0% 45%, #ffffff 0% 100%)}
  50%{background : conic-gradient(#bbbee6 0% 50%, #ffffff 0% 100%)}
  55%{background : conic-gradient(#bbbee6 0% 55%, #ffffff 0% 100%)}
  60%{background : conic-gradient(#bbbee6 0% 60%, #ffffff 0% 100%)}
  65%{background : conic-gradient(#bbbee6 0% 65%, #ffffff 0% 100%)}
  70%{background : conic-gradient(#bbbee6 0% 70%, #ffffff 0% 100%)}
  75%{background : conic-gradient(#bbbee6 0% 75%, #ffffff 0% 100%)}
  80%{background : conic-gradient(#bbbee6 0% 80%, #ffffff 0% 100%)}
  85%{background : conic-gradient(#bbbee6 0% 85%, #ffffff 0% 100%)}
  90%{background : conic-gradient(#bbbee6 0% 90%, #ffffff 0% 100%)}
  95%{background : conic-gradient(#bbbee6 0% 95%, #ffffff 0% 100%)}
  100%{background : conic-gradient(#bbbee6 0% 100%, #ffffff 100% 100%)}
}

#one {
  border: none;
  width: 300px;
  height: 80px;
  margin-left: 70px;
  font-size: 15pt;
  background: none;
  font-weight: bold;
  font-family: "MS Gothic";
}

#menu {
  text-align: left;
  margin-left: 100px;
  margin-top: 50px;
}

*{
  margin:0; padding:0;
  font-size:15px;
  line-height:1.3;
  color: black;
}

ul{
  list-style:none;
  text-align: left;
}
.tabmenu{
  
  position:relative;
}
.tabmenu ul{
  position: relative;
}
.tabmenu ul li{
  display:  inline-block;
  width:20%;
  float:left;
  text-align:center;
  background :#f9f9f9;
  line-height:40px;
}
.tabmenu label{
  display:block;
  width:100%;
  height:40px;
  line-height:40px;
}
.tabmenu input{display:none;}
.tabCon{
  display:none;
  width: 100%;
  height: 400px;
  text-align:left;
  padding: 20px;
  position:absolute;
  left:0; top:40px;
  box-sizing: border-box;
  border : 5px solid #f9f9f9;
}
.tabmenu input:checked ~ label{
  background:#bbbee6;
}
.tabmenu input:checked ~ .tabCon{
  display:block;
}

textarea:focus {
      outline: none;
    }

</style>