set terminal png font "Helvetica,9"
set output "pressure_comparison.png"
set key autotitle columnhead
unset key
set xlabel 'time_{unix} (s)'
set ylabel 'pressure (mbar)' 
plot 'pressure.tsv' w lp, 'pressure_ambient.tsv' w lp
