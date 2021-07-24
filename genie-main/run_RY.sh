for (( COUNTER=$1; COUNTER<=$2; COUNTER+=1 )); do
    echo "Submitting model: No. $COUNTER"
    qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh muffin.CBE.worlg4.BASESFeTDTL \
	 RUI_LABS/sensitivity ForamECOGEM-$COUNTER.config 150 Grigoratou.8P7Z1F.SPIN
done
