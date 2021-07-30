#!/bin/bash

SIZE=$(df --output=size -h / | sed -n '2p')
CPU=$(nproc)
MEM=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
HOSTNAME=$(hostname)
echo hostname is "$HOSTNAME", total memory="$MEM" kB, number of CPU="${CPU}", total disk size="${SIZE}" > file
