// ════════════════════════════════════════════════════════════
// KLARTEXT · supabase.js
// Supabase-Client-Initialisierung
//
// Setzt voraus, dass das Supabase-JS-SDK bereits geladen ist:
// <script src="https://unpkg.com/@supabase/supabase-js@2"></script>
//
// TODO: Platzhalter durch die echten Projekt-Zugangsdaten ersetzen
// (Supabase Dashboard → Project Settings → API). Der Anon-Key ist
// wie der bisherige Firebase-API-Key öffentlich sichtbar — der
// eigentliche Schutz kommt aus den Row-Level-Security-Policies in
// supabase/migrations/.
// ════════════════════════════════════════════════════════════

const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
