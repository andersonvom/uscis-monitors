#!/usr/bin/env bash

python="$HOME/.pyenv/shims/python"
CURRENT_DIR=$(cd $(dirname "$0") && pwd -P)

output=""

function run {
  local res=$($python "$1" "$2" "$3" "$4")
  if [ "$res" = "" ]; then
    return
  fi

  if [ "$output" != "" ]; then
    output="$output | $res"
  else
    output="$res"
  fi
}

function run_all {
  source $CURRENT_DIR/tasks
}

run_all

if [ "$output" != "" ]; then
  echo $output
else
  echo "No changes."
fi
