#!/usr/bin/env bash
data1=$(cat<<-EOF
INFO  get_systems_storage_container : No SAN StoragePools found in model.\n
INFO  list_snapshots                : NAS SNAP: No NAS snapshots found on the system (tag=Snapshot).\n
INFO  lms_snapshots                 : LVM SNAP: No LMS LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-svc-2 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-svc-3 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-svc-1 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-svc-4 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-svc-5 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  nodelocal_snapshots           : LVM SNAP: No cloud-db-1 LVM snapshots found on the system (tag=enm_upgrade_snapshot).\n
INFO  manage_enminst_snapshots      : ENM list_snapshot finished successfully\n
INFO  list_snapshot_names           : No modeled snapshots found.\n
INFO  manage_litp_snapshots         : ENM list_named finished successfully\n
INFO  list_snapshots                : No modeled snapshot called "snapshot" exists!\n
EOF
)



data2=$(cat<<-EOF
INFO  get_systems_storage_container : No SAN StoragePools found in model.\n
INFO  get_elasticsearch_active_host : Active elasticsearch node is cloud-db-1\n
INFO  remove_lms_snaphots           : LVM SNAP: Deleting LMS snapshots with tag @enm_upgrade_snapshot\n
INFO  remove_snapshots              : LVM MGR: Removing LVM snapshots with tag: enm_upgrade_snapshot\n
INFO  remove_lms_snaphots           : LVM SNAP: LMS : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: Reading available node local Logical Volumes.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-svc-2 : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-svc-3 : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-svc-1 : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-svc-4 : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-svc-5 : No LV snapshots found to delete.\n
INFO  remove_nodelocal_snapshots    : LVM SNAP: cloud-db-1 : No LV snapshots found to delete.\n
INFO  remove_snapshots              : NAS SNAP: Looking for rollbacks to destroy.\n
INFO  remove_snapshots              : NAS SNAP: No rollbacks to destroy, continuing.\n
INFO  remove_rollback_cache         : NAS SNAP: Looking for rollback caches to destroy.\n
INFO  remove_rollback_cache         : NAS SNAP: No rollback cache needs destroying.\n
INFO  ensure_removal_fs_not_required: NAS SNAP: Ensuring any filesystems marked for removal are not present on the NAS\n
INFO  get_filesystems_for_removal   : NAS SNAP: Determining list of filesytems for removal\n
INFO  manage_enminst_snapshots      : ENM remove_snapshot finished successfully\n
INFO  remove_litp_snapshots         : No modeled snapshot(s) exist!\n
INFO  manage_litp_snapshots         : ENM remove_snapshot finished successfully\n
EOF
)


if [[ $*  == "--action list_snapshot --snap_type=all" ]]; then
        echo -e $data1
	      exit 23
fi

if [[ $* == "--action remove_snapshot --snap_type=all" ]]; then
        echo -e $data2
fi

