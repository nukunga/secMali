// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAMIXnUkH83u6_AjqeF7fCEt5QoJbqVBSY",
  authDomain: "secmali.firebaseapp.com",
  projectId: "secmali",
  storageBucket: "secmali.appspot.com",
  messagingSenderId: "831156730742",
  appId: "1:831156730742:web:61cc337ce5a43bc0fa9857",
  measurementId: "G-EFK9S6VDPQ"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const analytics = getAnalytics(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
