all: run_exp1

run_exp1:
	qsub -j y -o cgenie_log -V -S /bin/bash runmuffin.sh cgenie.ebf_go_gs_ac_bg_eg.u067bc.BASES RUI_LABS/kpg muffin.u067bc.PO4.8P8Z.EXP1.$(wildcard) 200 muffin.u067bc.PO4.8P8Z.SPIN
