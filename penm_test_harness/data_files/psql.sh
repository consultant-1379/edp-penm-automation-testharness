#!/usr/bin/env bash

if [[ $* == "-h postgresql01 -d idenmgmt -U idenmgmt -qAt -c SELECT status FROM postgre_user WHERE name='administrator';" ]]; then
        echo "enabled"
fi
