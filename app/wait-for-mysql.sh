#!/bin/bash

set -e
set -x

host="$1"
cmd="$@"

until mysql --user="root" --password="admin123" --host="$host" --database="sys" --execute='select 1'; do
    >&2 echo "MySQL is unavailable - sleeping"
    sleep 4
done

>&2 echo "MySQL is up - executing command"
$2 $3 $4

>&2 echo "Keep python running"
exec $5 $6


