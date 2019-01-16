#!/usr/bin/env bash

python="$HOME/.pyenv/shims/python"
CURRENT_DIR=$(cd $(dirname "$0") && pwd -P)

function run {
  $python "$1" "$2" "$3" "$4"
}

function run_all {
  source $CURRENT_DIR/tasks
}

output=$(run_all | grep -ve '^$' | paste -sd '|' - | sed -e 's/\|/ | /g')

if [ "$output" != "" ]; then
  echo $output
else
  echo "No changes."
fi
