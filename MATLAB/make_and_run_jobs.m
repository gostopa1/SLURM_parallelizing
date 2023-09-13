ind=1000;
nojobs=220;

delete jobs/*
delete logs/*

% To run the example script by submitting each repetition as a separate job
ind=function_make_script_array(['test_script'],nojobs,ind)

% To run the example script by submitting an array of repetition
% ind=function_make_parallel_scripts(['test_script'],nojobs,ind)

make_slurm_run_jobs

system('./slurm_run_jobs_auto.sh ')
