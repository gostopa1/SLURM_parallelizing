import os
import argparse

os.makedirs('jobs',exist_ok = True)
os.makedirs('logs',exist_ok = True)

parser = argparse.ArgumentParser(description='Process some integers.')
# Add an argument
parser.add_argument('--script', type=str, default='echo "No command provided!"')
parser.add_argument('--jobind', type=int, default=0)
parser.add_argument('--noruns', type=int, default=10)

args = parser.parse_args()

script = args.script
jobind = args.jobind;
noruns = args.noruns

curpath = os.getcwd()

os.system('rm ' + curpath + ' /logs/*')
os.system('rm ' + curpath + '/jobs/*')

def function_make_script_array(script='echo "Test Run"',noruns=10,jobind=0):
    print('Making jobs...')
    curdir = os.getcwd()
    jobind=jobind+1
    f = open('jobs/job_' + str(jobind) + '.sh', 'w')
    f.write("#!/bin/bash\n\n")
    f.write("#SBATCH -t 1:59:59\n")
    f.write('#SBATCH --array=1-' + str(noruns) + '\n\n');
    f.write('#SBATCH -o ./logs/log_' + str(jobind) + '\n')
    f.write("#SBATCH --qos=normal\n\n")
    f.write("#SBATCH --mem-per-cpu=31000\n\n")
    f.write('echo' + script + '; cd '+ curpath + '; ' + script)
    f.close()
    return jobind

if __name__ == '__main__':
    make_jobs('echo "Testing SLURMMM..."', noruns=noruns, jobind=jobind)