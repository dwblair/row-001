#set yrange[2060:2260]
expt_start=1514345519.27
corrected_y_shift=945
pointSize=0.05
set ylabel('mbar')
set xlabel('hours')
set yrange[960:1120]
#set key left below Left
set title('pressure: probe, ambient, corrected')
set ytics 10
set mytics 5
set grid ytics lc rgb "#bbbbbb" lw 1 lt 0
plot 'pressure.tsv' using ($1-expt_start)/3600:2 title 'probe' ps pointSize, 'pressure_ambient.tsv' using ($1-expt_start)/3600:2 title 'ambient' ps pointSize, 'pressure_corrected.tsv' using ($1-expt_start)/3600:($2+corrected_y_shift) title '[probe-ambient] + 945 mbar' ps pointSize
