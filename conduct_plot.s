#expt_start=1514080973.7 #unixtime
#expt_start=1514354513.1
expt_start=1514410407.15
set terminal png size 1000 font "Helvetica,8"
set output "conductivity.png"
set key autotitle columnhead
unset key
set key
set xlabel 'time (hours)'
set ylabel 'conductivity (uS/cm)' 
set title 'Conductivity of solution in beaker'
set yrange[0:3500]
#plot 'conductivity.tsv' using 1:($2-2013)/0.2 w lp

#plot 'conductivity_specific.tsv' using ($1-expt_start)/3600:2 w p title "experiment", 900 title "900 uS/cm", 1413 title "1413 uS/cm^2", 2000 title "2000 uS/cm^2", 3000 title "3000 uS/cm^2"
plot 'conductivity_specific.tsv' using ($1-expt_start)/3600:2 w p title "experiment", 875 title "875 uS/cm", 925 title "925 uS/cm", 2500 title "2500 uS/cm", 3000 title "3000 uS/cm", 'conductivity_adc.tsv' using ($1-expt_start)/3600:2 w p title 'adc' 

