import { app, db } from "src/boot/firebase";
import { addDoc, collection, getDocs } from "firebase/firestore";

const querySnapshot = await getDocs(collection(db, "test"));

//test function that returns all documents from db collection 'test'
export function testFunction() {
  const testDocList = []

  querySnapshot.forEach((doc) => {
    const testDoc = {
      testDocId: doc.id,
      ...doc.data()
    }
    testDocList.push(testDoc)
  });

  return testDocList
}


export async function createFileDoc(fileRef) {
  try {
    const docRef = await addDoc(collection(db, "fileUpload"), { download_url: fileRef });
    return docRef.id;
  } catch (e) {
    console.error('Error creating file doc : ', e);
    throw e;
  }
}
