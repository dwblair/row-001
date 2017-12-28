expt_start=1513830545.11
set terminal png size 1000 font "Helvetica,8"
set output "pressure_comparison.png"
set key autotitle columnhead
unset key
set key
set xlabel 'time (hours)'
#set xlabel 'time (days)'
set ylabel 'pressure (mbar)' 
set title 'Pressure: bottom-of-bucket and ambient'
plot 'pressure.tsv' using ($1-expt_start)/3600:2 w lp title "bottom-of-bucket", 'pressure_ambient.tsv' using ($1-expt_start)/3600:2 w lp title "ambient"
#plot 'pressure.tsv' using ($1-expt_start)/(3600*24):2 w lp, 'pressure_ambient.tsv' using ($1-expt_start)/(3600*24):2 w lp
