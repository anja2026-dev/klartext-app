import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const supabaseUrl = "https://lrrnieagkqjedaakhwhi.supabase.co";
const supabaseKey = "sb_publishable_Aw5XKMDedxL74T-xTbtb3Q_y1PiaJ57";

export const supabase = createClient(supabaseUrl, supabaseKey);
