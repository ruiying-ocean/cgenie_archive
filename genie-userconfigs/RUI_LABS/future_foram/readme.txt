---------  Step 1 Run spinup (0-10000) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worjh2.BASESFeTDTL.Albani  RUI_LABS/future_foram worjh2.RpCO2_Rp13CO2.Albani.0ka.SPIN 10000

--------- Step 2 Run historical (1765-2022) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worjh2.BASESFeTDTL.Albani  RUI_LABS/future_foram worjh2.RpCO2_Rp13CO2.Albani.0ka.historical 257 worjh2.RpCO2_Rp13CO2.Albani.0ka.SPIN

--------- Step 3 Run future (2022-2100) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worjh2.BASESFeTDTL.Albani  RUI_LABS/future_foram worjh2.RpCO2_Rp13CO2.Albani.2100.[XXX]deg worjh2.RpCO2_Rp13CO2.Albani.0ka.historical

