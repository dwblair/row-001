#set yrange[2060:2260]
expt_start=1514410407.15
set ylabel('adc')
set xlabel('hours')
set title('recovery after placed in higher-conductivity solution and not rinsed')
plot 'conductivity_adc.tsv' using ($1-expt_start)/3600:2 title 'conductivity_{adc}', 2100 title '2100', 2080 title '2080'
