--------- 1.1 Run pre-industrial spinup (0-10000) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL RUI_LABS/foramecogem muffin.CBE.worlg4.BASESFeTDTL.foramecogem2.1.SPIN 10000

--------- 1.2 Run historical (1765-2022) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL RUI_LABS/foramecogem muffin.CBE.worlg4.BASESFeTDTL.foramecogem2.1.historical 257 muffin.CBE.worlg4.BASESFeTDTL.foramecogem2.1.SPIN
--------- 1.3 Run future (2022-2100) --------- 

qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL RUI_LABS/foramecogem muffin.CBE.worlg4.BASESFeTDTL.foramecogem2.1.2100.[XXX]deg 78 muffin.CBE.worlg4.BASESFeTDTL.foramecogem2.1.SPIN

--------- 2 Run LGM spinup --------- 
qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CB.GIteiiva.BASESFeTDTL_rb_ecogem RUI_LABS/foramecogem muffin.CBE.GIteiiva.BASESFeTDTL_rb_foramecogem2.1 10000
