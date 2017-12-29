expt_start=1514345519.27
#set yrange[1020:1090]
set xlabel('hours')
set ylabel('mbar')
set yrange[0:100]
plot 'pressure_corrected.tsv' using ($1-expt_start)/3600:2 title 'ambient-corrected pressure at bottom of bucket', 40 title '40 mbar', 50 title '50 mbar'

