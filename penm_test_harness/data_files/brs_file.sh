#!/usr/bin/env bash

data=$(cat<<-EOF
{
    "backup_finish_time": null,
    "backup_start_time": null,
    "key": null,
    "nas_bkup_node": null,
    "pid": null,
    "spn": null,
    "status": "UNKNOWN",
    "tag": null
}
EOF
)
if [[ $* == "backup_status --tag ombs" ]]; then
        echo $data
fi
