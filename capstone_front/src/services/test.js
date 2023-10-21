import { app, db } from "src/boot/firebase";
import { collection, getDocs } from "firebase/firestore";

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
