#set yrange[2060:2260]
expt_start=1514345519.27
set ylabel('mbar')
set xlabel('hours')
set yrange[1010:1100]
set title('pressure: bucket probe and ambient')
#plot 'pressure.tsv' using ($1-expt_start)/3600:2 title 'conductivity_{adc}', 2100 title '2100', 2080 title '2080'
plot 'pressure.tsv' using ($1-expt_start)/3600:2 title 'probe at bucket bottom', 'pressure_ambient.tsv' using ($1-expt_start)/3600:2 title 'ambient pressure', 1052 title 'probe at top of bucket', 1080 title '1080', 1070 title '1070'
