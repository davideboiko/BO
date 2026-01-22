// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth"; 
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAmSERpNNKSNL58MselGCtjEafQHeiu0yg",
  authDomain: "user-crud-df779.firebaseapp.com",
  projectId: "user-crud-df779",
  storageBucket: "user-crud-df779.firebasestorage.app",
  messagingSenderId: "963050961877",
  appId: "1:963050961877:web:158f79db07885632595b5c"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export {app, db, auth};