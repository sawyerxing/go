#!/bin/sh

#go through each line
#if contains m, then append column m
#if contains v, then append column v
#if contains both m and v, then append both
#example:
#input.tsv
#BMXMM05v177390,BMXMM05m850489,BMXMF05m1502543,BMXFM08v283599p1
#QHF9FF09m445338,QHF9FF09v449482
#DBFM03m13735p1,DBFM04v1061706,BMXFF06v464492
#NWMF02v251332,NWMF02m453866
#SWFF04v178528,SWFM04v103976,BMXMF10m1200151,BMXMM10v303699,BMXMF10v79091,BMXMM05v115874
#QHF9FM09m182433,QHF9FH09v411361,QHF9FH09m210258
#outputfile
#BMXMM05v177390,BMXMM05m850489,BMXMF05m1502543,BMXFM08v283599p1 both
#QHF9FF09m445338,QHF9FF09v449482 both
#DBFM03m13735p1,DBFM04v1061706,BMXFF06v464492 both
#NWMF02v251332,NWMF02m453866 both
#SWFF04v178528,SWFM04v103976,BMXMF10m1200151,BMXMM10v303699,BMXMF10v79091,BMXMM05v115874 both
#QHF9FM09m182433,QHF9FH09v411361,QHF9FH09m210258 both
function check_m_v() {
	local inputfile=$1
	local outputfile="./outputfile"
	# clean the outputfile first
	rm ${outputfile}
	for eachline in `cat ${inputfile}` 
	do
		if [[ ${eachline} =~ "m" ]] && [[ ${eachline} =~ "v" ]] ; then
			echo "${eachline} both" >> ${outputfile}
		elif [[ ${eachline} =~ "m" ]] ; then
			echo "${eachline} m" >> ${outputfile}
		elif [[ ${eachline} =~ "v" ]] ; then
			echo "${eachline} v" >> ${outputfile}
		else
			echo "ERROR"
		fi
	done
}

function main() {
	check_m_v "./input.tsv"
}

main $*
