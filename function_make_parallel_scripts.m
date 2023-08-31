function jobind=function_make_parallel_scripts(scriptToRun,noruns,stind)

%Make output directories if needed
mkdir jobs
mkdir logs

jobind=stind;
display('Making jobs ...')

% How many repetitions to run
for repsi=1:noruns
    jobind=jobind+1;
    fid = fopen(['./jobs/job_' num2str(jobind) '.sh'],'w');

    fprintf(fid,'#!/bin/bash\n\n');

    fprintf(fid,'#SBATCH -p batch\n');
    fprintf(fid,'#SBATCH -t 1:59:59\n'); %  Time limits
    fprintf(fid,['#SBATCH -o "' './logs/log_' num2str(jobind) '"\n']); % Log to store the outputs
    fprintf(fid,'#SBATCH --qos=normal\n\n'); % Priority
    fprintf(fid,'#SBATCH --mem-per-cpu=31000\n\n'); % Maximum memory per job

    % Submit the current job, run in MATLAB no GUI mode, cd to current
    % directory, initialize the random seed and run the requested script.
    % Then exit
    fprintf(fid,['matlab -nojvm -r "cd ' pwd '/;rng(' num2str(randi(100000)) ');' scriptToRun ';exit;"']); % for 32mm

    fclose(fid);
end
display('Done making jobs!')
end