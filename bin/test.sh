#!/bin/bash
source `dirname $0`/env.sh

python $BASE_DIR/shop/manage.py test $*
