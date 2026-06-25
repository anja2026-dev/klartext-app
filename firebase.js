// Firebase-Konfiguration
const firebaseConfig = {
  apiKey: "AIzaSyBAvwxOT2wCTFJr2u4itLQxcs9Lo5lrHwU",
  authDomain: "klartext-mentoring.firebaseapp.com",
  databaseURL: "https://klartext-mentoring-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "klartext-mentoring",
  storageBucket: "klartext-mentoring.firebasestorage.app",
  messagingSenderId: "1091821217777",
  appId: "1:1091821217777:web:be7707d4b3a43710ee4650"
};

// Firebase initialisieren
firebase.initializeApp(firebaseConfig);
const db = firebase.database();

// Weiterleitung speichern
function sendForward(data) {
  return db.ref("forward").push({
    ...data,
    timestamp: Date.now()
  });
}

// Weiterleitungen für eine Rolle abrufen
function getInbox(role, callback) {
  db.ref("forward")
    .orderByChild("targetRole")
    .equalTo(role)
    .on("value", (snapshot) => {
      callback(snapshot.val() || {});
    });
}
