#!/usr/bin/env bash


lib_path=${EASYOPS_COLLECTOR_dm_bin_path}

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${lib_path}

BASEDIR=$(dirname $0)
python $BASEDIR"/collector.py"
