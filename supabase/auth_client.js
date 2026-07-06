import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const supabaseUrl = "https://wtfsrgxwhdugtyuurhsh.supabase.co";
const supabaseKey = "sb_publishable_SxAMtQ6b42My1Yh2ap5Cfw_pnxFWbwa";

export const supabase = createClient(supabaseUrl, supabaseKey);
