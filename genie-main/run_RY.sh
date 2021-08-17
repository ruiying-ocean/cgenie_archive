for (( COUNTER=$1; COUNTER<=$2; COUNTER+=1 )); do
    echo "Submitting model: No. $COUNTER"
    qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worjh2.BASESFeTDTL.Albani\
	 RUI_LABS/sensitivity_Albani ForamECOGEM-$COUNTER.config 300 test-64.config
done
