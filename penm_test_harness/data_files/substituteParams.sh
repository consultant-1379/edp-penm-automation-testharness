#!/usr/bin/env bash

data1=$(cat<<-EOF
INFO  substitute                    : Substituting parameters...
INFO  substitute                    : SED file set to /tmp/ansible_tmp_sed.txt
INFO  substitute                    : XML Template set to /ericsson/deploymentDescriptions/medium/medium__production_5svc_streaming-vapp-ssgid_ipv6_cloud_test_dd.xml
INFO  build_param_file              : Reading contents of /root/.ssh/vm_private_key.pub
INFO  verify_xml                    : Successfully substituted all parameters
INFO  write_file                    : Fully populated xml can be found in /opt/ericsson/enminst/runtime/enm_deployment.xml
EOF
)

echo -e $data1
