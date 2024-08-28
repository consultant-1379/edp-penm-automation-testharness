#!/usr/bin/env bash

base_path='/software/testharness_data_files'

if [[ $* == "-h 10.232.88.6 -user admin -password Password123_ -Scope 0 storagepool -list -name ENMtest" ]]; then
        echo -n `cat $base_path/ms_get_storagepool_disks.txt`

elif [[ $* == "-h 10.232.88.6 -user localadmin -password Password123_ -Scope 0 getagent" ]]; then
       echo -n `cat $base_path/ms_get_vnx_model.txt`

elif [[ $* == "-h 10.144.110.14 -user admin -password password -Scope 0 storagepool -feature -info -availableDisks" ]]; then
      echo -n `cat $base_path/get_available_disks.txt`

elif [[ $* == "-h 10.144.110.14 -user admin -password password -Scope 0 hotsparepolicy -list" ]]; then
      echo -n `cat $base_path/ms_get_hotspare_policy.txt`

elif [[ $* == "-h 10.144.110.14 -user admin -password password -Scope 0 storagepool -list -name ENMtest -rtype" ]]; then
      echo -n `cat $base_path/ms_get_raid_type.txt`
elif [[ $* == "-h 10.144.110.14 -user admin -password password -Scope 0  storagepool -expand -name ENMtest -disks "* ]]; then
      echo -n `sh $base_path/update_get_storagepool_disks.sh $base_path`
fi
