#!/usr/bin/env bash

function db_get() {
    grep "$1," database | sed -e /^$1,// | tail -n
}

function db_set() {
    echo "$1,$2" >> database
}
