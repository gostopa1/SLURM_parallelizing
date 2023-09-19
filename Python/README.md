## Description
A collection of scripts and functions to submit jobs in SLURM workload manager.

See main example `make_and_run_jobs.py`

## Details

* `function_make_parallel_script`
    *   Function to generate SLURM jobs to run a specific command. May run also with command line arguments e.g. 
    `python function_make_parallel_script.py --script "echo job" --jobind 50 --noruns 100`
    * This command makes 100 jobs that run the command `echo job`. The numbering of the jobs start from 50.
    
    *   Input arguments:
        * `script`: a string that corresponds to the matlab script that needs to be run. E.g. '`echo "Hey you"`'
        * `jobind` The starting index of the submitted job. It is incremented for each job (see Output arguments for context)
        * `noruns`: how many repetitions to run
        the script above
        
    * Output arguments:
        * `jobind`: the last index of the submitted job. Used to continue submitting more jobs in a for loop

* `function_make_script array.py`
    * Same as above but submits an array of jobs instead. See [SLURM documentation for more details on job arrays](https://slurm.schedmd.com/job_array.html)


* `make_slurm_run_jobs.py`
    * creates a bash script `slurm_run_jobs.sh` that runs all jobs under the `./jobs/` directory.
    See how `make_and_run_jobs` script uses the script, or run it by running `source make_run_jobs.sh`

* `make_and_run_jobs.py`
    * creates and submits jobs to SLURM work manager. The example runs makes 10 repetitions of the `test_script` as jobs inside the `jobs` directory and runs the jobs. The logs of these jobs are stored under the `./logs` directory


* `test_script.py`
    * Script to use as an example for submitting jobs. It generates a random integer assigned to a variable `a` and it saves that variable in a `.mat` file with a filename corresponding to the random integer (e.g. `18390.mat`)
