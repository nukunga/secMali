import { firebase } from 'boot/firebase'
import axios from 'axios'

// Firebase 설정
const storage = firebase.storage()
const firestore = firebase.firestore()

// 파일 업로드 함수
async function uploadFile(file) {
  // Storage에 파일 업로드
  const storageRef = storage.ref()
  const fileRef = storageRef.child(file.name)
  await fileRef.put(file)

  // 업로드한 파일의 URL 가져오기
  const fileUrl = await fileRef.getDownloadURL()

  // Firestore에 파일 정보 저장
  const docRef = firestore.collection('files').doc()
  await docRef.set({
    name: file.name,
    url: fileUrl
  })

  // 백엔드 API 호출
  const response = await axios.post('https://your-backend-api.com/documents', {  //백엔드 주소 기입
    documentId: docRef.id
  })

  return response.data
}

// submit 이벤트 처리 함수
async function handleSubmit() {
  const fileInput = document.getElementById('uploadFile')
  if (fileInput.files.length > 0) {
    const file = fileInput.files[0]
    await uploadFile(file)
  }
}