#!/usr/bin/env bash
sleep 1

if [[ $*  == "--action enminst_healthcheck" ]]; then
        echo "Successfully Completed ENM System Healthcheck"
fi

if [[ $* == "--action node_fs_healthcheck" ]]; then
        echo "Successfully Completed Node Filesystem Healthcheck"
fi
