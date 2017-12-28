expt_start=1513830545.11
set terminal png size 1000 font "Helvetica,9"
set output "temp_comparison.png"
set key autotitle columnhead
unset key
set key
set xlabel 'time (hours)'
set ylabel 'temp (C)' 
set title 'Temp: bottom-of-bucket and ambient'
plot 'temp.tsv' using ($1-expt_start)/3600:2 w lp title "bottom-of-bucket", 'temp_ambient.tsv' using ($1-expt_start)/3600:2 w lp title "ambient"
