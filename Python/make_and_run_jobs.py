from function_make_script_array import function_make_script_array
from function_make_parallel_scripts import function_make_parallel_scripts
from make_slurm_run_jobs import make_slurm_run_jobs
import os 
ind=1000;
nojobs=10;

curpath = os.getcwd()

os.system('rm ' + curpath + ' /logs/*')
os.system('rm ' + curpath + '/jobs/*')


# To run the example script by submitting each repetition as a separate job
# ind=function_make_script_array('python test_script.py',nojobs,ind)

# To run the example script by submitting an array of repetition
ind=function_make_parallel_scripts('python test_script.py',nojobs,ind)

make_slurm_run_jobs

os.system('./slurm_run_jobs_auto.sh ')
