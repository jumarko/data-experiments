#!/usr/bin/env bash

function db_get() {
    grep "$1," database | sed -e "s/^$1,//" | tail -n 1
}

function db_set() {
    echo "$1,$2" >> database
}
