set terminal png size 1000 font "Helvetica,8"
set output "conductivity.png"
set key autotitle columnhead
unset key
set xlabel 'time_{unix} (s)'
set ylabel 'conductivity (uS)' 
plot 'conductivity.tsv' using 1:($2-2013)/0.2 w lp
