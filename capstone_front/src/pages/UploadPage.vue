<template>
  <q-page id="main" class="scroll">
    <div id='wrap'>
        <div class="hero-banner">
    <div class="text-center preview-description">
        <h1>SecMali</h1>
			  <small style="font-style: oblique">Document Analysis Program</small>
    </div>
</div>
<div id="wrap1">
    <div id='form_wrap'>
      <form ref="formRef">
        <br>
        <div class="flex flex-center">
        <q-uploader
        ref="uploader"
        url="https://secmali.web.app/#/"
        color="indigo-9"
        accept=".hwp, .doc, .xlsx"
        flat
        bordered
        style="width: 600px; margin-top:100px; margin-bottom: 20px;"
        @added="uploadFile"
        icon.onclick="location.href='loading'"
      />
    </div>
    <p style="text-align: center; font-size: medium;">Drag & drop file here <br>or browse file from device</p>
      </form>
    </div>
  </div>
</div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { ref as firebaseStorageRef, getDownloadURL, uploadBytes } from 'firebase/storage';
import { api } from 'src/boot/axios';
import { createFileDoc } from '../services/test'
import { storage } from 'src/boot/firebase';
import {v4} from "uuid"

export default defineComponent({
  name: 'UploadPage',
  setup() {
    const formRef = ref();
    const storageRef = firebaseStorageRef(storage, "files");
    const fileModel = ref();
    const uploadedFileUrl = ref();

    async function uploadFile() {
      console.log(fileModel.value)
      await uploadFileToStorage()

      const res = await createFileDoc(uploadedFileUrl.value);

      api.post('http://43.201.179.16:8000/analyze_document', {document_id: res}).then((res) => {
        console.log(res);
      })
    }

    async function uploadFileToStorage() {
      const fileRef = firebaseStorageRef(storageRef, fileModel.value.name + v4());
      return uploadBytes(fileRef, fileModel.value).then((snapshot) => {
         return getDownloadURL(snapshot.ref).then((url) => {
          uploadedFileUrl.value = url;
          return url
        })
      })
    }

    return {
      formRef,
      fileModel,
      uploadFile,
    }
  }
})
</script>

<style scoped>

.scroll {
    overflow: hidden;
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
  height: auto;
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

#wrap {
    width:530px; margin:20px auto 0; height:1000px;
}
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


    body, div, h1,h2, form, fieldset, input, textarea, footer,p {
      margin: 0; padding: 0; border: 0; outline: none;
    }

    body {background: white; color: #7c7873;}
    p {text-shadow:0 1px 0 #fff; font-size:24px;}
    #wrap1 {width:530px; margin:20px auto 0;}

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

    #form_wrap { overflow:hidden; height:446px; position:relative; top:0px;
      -webkit-transition: all 1s ease-in-out .3s;
      -moz-transition: all 1s ease-in-out .3s;
      -o-transition: all 1s ease-in-out .3s;
      transition: all 1s ease-in-out .3s;}

    #form_wrap:before {content:"";
      position:absolute;
      bottom:128px;left:0px;
      background:url('~assets/before.png');
      width:530px;height: 316px;}

    #form_wrap:after {content:"";position:absolute;
      bottom:0px;left:0;
      background:url('~assets/after.png');
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

</style>
