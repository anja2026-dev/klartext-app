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

// Anonyme Firebase-Auth-Anmeldung (Stufe 1 der Absicherung, siehe Analyse).
// Transparent, kein UI, kein sichtbares Login für Nutzer - läuft nur intern,
// damit "auth" für Firebase-Regeln nicht mehr grundsätzlich null ist. db und
// alle db.ref(...)-Aufrufe bleiben sofort synchron nutzbar (Referenzen
// erzeugen selbst keinen Netzwerk-Request); das Firebase-SDK verknüpft
// offene Verbindungen automatisch mit dem Anmeldestatus, sobald
// signInAnonymously() abgeschlossen ist - kein Warten an den einzelnen
// Aufrufstellen nötig. Setzt voraus, dass "Anonymous" als Sign-in-Methode
// in der Firebase-Konsole (Authentication → Sign-in method) aktiviert ist.
firebase.auth().signInAnonymously().catch(function(fehler) {
  console.error('Anonyme Firebase-Anmeldung fehlgeschlagen:', fehler);
});

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
