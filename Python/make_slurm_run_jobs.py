import os
import argparse

curpath = os.getcwd()

def make_slurm_run_jobs(curpath):
    f = open('slurm_run_jobs_auto.sh','w');
    f.write('#!/bin/sh\n\n');
    f.write('chmod 755 ' + curpath + '/jobs/*\n\n');
    f.write('# This is the part where we submit the jobs that we cooked\n\n');
    f.write('for j in $(ls -1 ' + curpath + '"/jobs/");do\n');
    f.write('sbatch ' + curpath + '"/jobs/"$j\n',);
    f.write('sleep 0.01\n');
    f.write('done\n');
    f.write('echo "All jobs submitted"\n\n');
    f.close();
    os.system('chmod 755 slurm_run_jobs_auto.sh');


if __name__ == '__main__':
    make_slurm_run_jobs(curpath=curpath)
