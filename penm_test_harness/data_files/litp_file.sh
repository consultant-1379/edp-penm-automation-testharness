#!/bin/bash

base_path='/software/testharness_data_files'
if [[ $1 == "version" ]]; then
    echo CXP9030418
fi

if [[ $* == "show -p /infrastructure/storage/storage_providers/san1/ -o san_type" ]]; then
   echo "vnx2"
fi

if [[ $* == "show -p /software/items/config_manager/global_properties -j" ]]; then
   cat $base_path/edp_req_global_props.txt
fi

if [[ $* == "show -p /plans -j" ]]; then
  cat $base_path/get_litp_plans.txt
fi

if [[ $* == "show_plan -j" ]]; then
  cat $base_path/get_litp_plan_details.txt
fi

if [[ $* == "show -p /deployments/enm/clusters/db_cluster/services/postgres_clustered_service/ -j" ]]; then
   cat $base_path/postgress.txt
fi

if [[ $* == "show -p /deployments/enm/clusters/db_cluster/nodes -j" ]]; then
    cat $base_path/db_cluster.txt
fi

if [[ $* == "show -p /deployments/enm/clusters -j" ]]; then
    cat $base_path/str_cluster.txt
fi

if [[ $* == "show -p /deployments/enm/clusters/str_cluster/nodes -j" ]]; then
    cat $base_path/str_cluster_nodes.txt
fi

if [[ $* == "show -p /infrastructure/storage/storage_providers/sfs -j" ]]; then
    cat $base_path/nas_prop_data.txt
fi
