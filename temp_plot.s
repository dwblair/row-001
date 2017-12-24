set terminal png size 1000 font "Helvetica,9"
set output "temp_comparison.png"
set key autotitle columnhead
unset key
set xlabel 'time_{unix} (s)'
set ylabel 'temp (C)' 
plot 'temp.tsv' w lp, 'temp_ambient.tsv' w lp
