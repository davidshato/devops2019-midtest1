#!/bin/bash


USAGE(){
	echo "`basename $0` USAGE: <DIR> <WORD>"
	exit 1
}


if [[ $# != 2 ]];
then
	USAGE
fi

if [[ $1 == "" ]];
then 
	USAGE
fi

if [[ $2 == "" ]];
then
	USAGE
fi



if [[ ! -d $1 ]];
then
	USAGE
fi



dir_name=$1
search_word=$2

find  $dir_name -type f | xargs grep -l $search_word
exit 0

