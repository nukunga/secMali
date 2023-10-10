<template>
  <q-page class="q-pa-xl">
    <p style="text-align: center">
    <img id="name" draggable="false" src="~assets\secmali_name.png" width="300">
    </p>
    <div id="explain" class="text-center text-h6">
        의심러운 파일을 분석하여 악성코드 및 기타 침해를 탐지합니다.
    </div>
    <div id="wrap">
      <div id='form_wrap'>
        <form action="" enctype="multipart/form-data" method="post">
          <br>
          <div class="flex flex-center">
          <input type="file" style="display : none;" name="uploadFile">
          <img src="~assets/secmali_open.png" name="fileupload2" onclick="document.all.uploadFile.click(); document.all.uploadFile.value=document.all.fileupload2.value" width="370">
          </div>
          <br><br>
          <input type="submit" name ="text" value="SecMali" style="color: #bbbee6; font-weight: bold; font-size: large"/>
        </form>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'IndexPage'
})
</script>
<style scoped>


body, div, h1,h2, form, fieldset, input, textarea, footer,p {
  margin: 0; padding: 0; border: 0; outline: none;
}

body {background: white; color: #7c7873;}
p {text-shadow:0 1px 0 #fff; font-size:24px;}
#wrap {width:530px; margin:20px auto 0; height:1000px;}

#form_wrap { overflow:hidden; height:446px; position:relative; top:0px;
  -webkit-transition: all 1s ease-in-out .3s;
  -moz-transition: all 1s ease-in-out .3s;
  -o-transition: all 1s ease-in-out .3s;
  transition: all 1s ease-in-out .3s;}

#form_wrap:before {content:"";
  position:absolute;
  bottom:128px;left:0px;
  background:url('../assets/before.png');
  width:530px;height: 316px;}

#form_wrap:after {content:"";position:absolute;
  bottom:0px;left:0;
  background:url('../assets/after.png');
  width:530px;height: 260px; }

#form_wrap.hide:after, #form_wrap.hide:before {display:none; }
#form_wrap:hover {height:776px;top:-200px;}

form {background:white;
  position:relative;top:200px;overflow:hidden;
  height:200px;width:400px;margin:0px auto;padding:20px;
  border: 1px solid #fff;
  border-radius: 10px;
  -moz-border-radius: 3px; -webkit-border-radius: 3px;
  box-shadow: 0px 0px 3px #9d9d9d, inset 0px 0px 27px #fff;
  -moz-box-shadow: 0px 0px 3px #9d9d9d, inset 0px 0px 14px #fff;
  -webkit-box-shadow: 0px 0px 3px #9d9d9d, inset 0px 0px 27px #fff;
  -webkit-transition: all 1s ease-in-out .3s;
  -moz-transition: all 1s ease-in-out .3s;
  -o-transition: all 1s ease-in-out .3s;
  transition: all 1s ease-in-out .3s;}


#form_wrap:hover form {height:530px;}

label {
  margin: 11px 20px 0 0;
  font-size: 16px; color: #b3aba1;
  text-transform: uppercase;
  text-shadow: 0px 1px 0px #fff;
}

input[type=text], textarea {
  font: 14px normal normal uppercase helvetica, arial, serif;
  color: #7c7873;background:none;
  width: 380px; height: 36px; padding: 0px 10px; margin: 0 0 10px 0;
  border:1px solid #f8f5f1;
  -moz-border-radius: 5px; -webkit-border-radius: 5px; border-radius: 5px;
  -moz-box-shadow: inset 0px 0px 1px #726959;
  -webkit-box-shadow:  inset 0px 0px 1px #b3a895;
  box-shadow:  inset 0px 0px 1px #b3a895;
}

textarea { height: 80px; padding-top:14px;}

textarea:focus, input[type=text]:focus {background:rgba(255,255,255,.35);}

#form_wrap input[type=submit] {
  position:relative;
  font-size:24px; color: #7c7873;text-shadow:0 1px 0 #fff;
  width:100%; text-align:center;opacity:0;
  background:none;
  cursor: pointer;
  -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px;
  -webkit-transition: opacity .6s ease-in-out 0s;
  -moz-transition: opacity .6s ease-in-out 0s;
  -o-transition: opacity .6s ease-in-out 0s;
  transition: opacity .6s ease-in-out 0s;
}

#form_wrap:hover input[type=submit] {z-index:1;opacity:1;
  -webkit-transition: opacity .5s ease-in-out 1.3s;
  -moz-transition: opacity .5s ease-in-out 1.3s;
  -o-transition: opacity .5s ease-in-out 1.3s;
  transition: opacity .5s ease-in-out 1.3s;}

#form_wrap:hover input:hover[type=submit] {color:#435c70;}
</style>