expt_start=1514080973.7
set yrange[2200:2400]
set xlabel('hours')
set ylabel('adc')
set title('conductivity experiment before decoupling')
plot 'conductivity_upto_2017_12_26.tsv' using ($1-expt_start)/3600:2, 2300 title '2300', 2280 title '2280'
