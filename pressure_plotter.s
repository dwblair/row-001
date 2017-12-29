expt_start=1514345519.27
set yrange[1000:1100]
set xlabel('hours')
set ylabel('mbar')
plot 'pressure_ambient.tsv' using ($1-expt_start)/3600:2 title 'ambient pressure', 'pressure.tsv' using ($1-expt_start)/3600:2 title 'pressure at bottom of bucket', 1070 title '1070 mbar', 1080 title '1080 mbar'

