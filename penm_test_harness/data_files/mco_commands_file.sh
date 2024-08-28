#!/usr/bin/env bash

base_path='/software/testharness_data_files'

if [[ $* == "find --json --no-progress" ]]; then
    echo -n `cat $base_path/mco_no_progress.txt`
elif [[ $* == "rpc rpcutil get_data source=resource --json --no-progress" ]]; then
    echo -n `cat $base_path/mco_get_data.txt`
elif [[ $* == "rpc edpautodeploy get_idenmgmt_user_pass_key -I cloud-db-1 -j" ]]; then
    cat $base_path/mco_rpc_cmd_output.txt
elif [[ $* == "rpc edpautodeploy vxdisk_list -I cloud-db-1 -j" ]]; then
    cat $base_path/mco_verify_disk.txt
fi
