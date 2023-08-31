ind=1000;
nojobs=220;

delete jobs/*
delete logs/*

% To run an example script
ind=function_make_script_array(['test_script'],nojobs,ind)

make_slurm_run_jobs

system('./slurm_run_jobs_auto.sh ')
