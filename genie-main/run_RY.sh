for (( COUNTER=$1; COUNTER<=$2; COUNTER+=1 )); do
    echo "Submitting model: No. $COUNTER"
    qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL\
	 RUI_LABS/Sensitivity ForamECOGEM-$COUNTER.config 500 8P7Z4F_respir_scheme

    ## For Albani basic config
    # qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worjh2.BASESFeTDTL.Albani.config\
    # 	 RUI_LABS/Sensitivity ForamECOGEM-$COUNTER.config 500 8P7Z4F_respir_scheme_Albani

done
