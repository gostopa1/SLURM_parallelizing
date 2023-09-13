% Simple matlab script to run as an example
a=randi(10000);
mkdir results
save(['results/' num2str(a) '.mat'],'a')
