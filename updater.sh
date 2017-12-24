#!/bin/bash

echo 'getting dat ...'
./dat_get.sh
echo 'updating graphs ...'
./pressure_plotter.sh
./temp_plotter.sh
./conduct_plotter.sh
display pressure_comparison.png&
display temp_comparison.png&
display conductivity.png&
