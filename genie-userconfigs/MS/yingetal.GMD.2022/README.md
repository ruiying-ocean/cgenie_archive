# About
For "ForamEcoGENIE 2.0: Incorporating symbiosis and spine traits into a trait-based global planktic foraminifera model", GMD, Rui Ying, Fanny M. Monteiro, Jamie D. Wilson, Daniela N. Schmidt

# Observational dataset
ForCenS, https://www.nature.com/articles/sdata2017109
plankton net, plankton_tow_grouped.csv
sediment trap, sediment_trap_grouped.csv

# Code
- 8P7Z4F, main output
- 8P7Z4F, seasonal output
- 8P7Z4F.zoo the ecosystem grazing file defining foraminifer feeding/spine trait

# Model experiments
```sh
# main experiment
qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL work_directory 8P7Z4F 10000
# monthly output
qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL work_directory 8P7Z4F_monthly 100 8P7Z4F
```