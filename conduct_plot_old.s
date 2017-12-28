expt_start=1514080973.7 #unixtime
set terminal png size 1000 font "Helvetica,8"
set output "conductivity.png"
set key autotitle columnhead
unset key
set key
set xlabel 'time (hours)'
set ylabel 'conductivity (uS/cm^2)' 
set title 'Conductivity of solution in beaker'
set yrange[0:3500]
#plot 'conductivity.tsv' using 1:($2-2013)/0.2 w lp
#plot 'conductivity.tsv' using 1:($2-2013)/0.2 w lp, 900 title "900 uS/cm^2", 1413 title "1413 uS/cm^2", 2000 title "2000 uS/cm^2", 3000 title "3000 uS/cm^2"
plot 'conductivity.tsv' using ($1-expt_start)/3600:($2-2013)/0.2 w lp title "experiment", 900 title "900 uS/cm^2", 1413 title "1413 uS/cm^2", 2000 title "2000 uS/cm^2", 3000 title "3000 uS/cm^2"

