#!/bin/bash
source `dirname $0`/env.sh

echo $DJANGO_SETTINGS_MODULE

cd $BASE_DIR
pre-commit run --all-files
