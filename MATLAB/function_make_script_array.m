function jobind=function_make_script_array(scriptToRun,noruns,stind)

%Make output directories if needed
mkdir jobs
mkdir logs

jobind=stind;
display('Making jobs ...')

jobind=jobind+1;
fid = fopen(['./jobs/job_' num2str(jobind) '.sh'],'w');

fprintf(fid,'#!/bin/bash\n\n');

fprintf(fid,'#SBATCH -p batch\n');
fprintf(fid,'#SBATCH -t 1:59:59\n'); %  Time limits
fprintf(fid,['#SBATCH --array=1-' num2str(noruns) '\n\n']); % How many repetitions in the array?
fprintf(fid,['#SBATCH -o ' './logs/log_' num2str(jobind) '_%%a\n']);
fprintf(fid,'#SBATCH --qos=normal\n\n');
fprintf(fid,'#SBATCH --mem-per-cpu=10000\n\n');

fprintf(fid,'sleep .$[( $RANDOM %% 10 ) ]s\n\n'); % Sleep for a random amount of time, so that the rng will give different seed
fprintf(fid,['matlab -nojvm -r "cd ' pwd '/;rng(''shuffle'');' scriptToRun ';exit;"']); % for 32mm

fclose(fid);
display('Done making jobs!')
end