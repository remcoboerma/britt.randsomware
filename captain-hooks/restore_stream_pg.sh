#!/bin/bash
source __tinkerbell__.sh

echorun restic $HOST -r $URI restore latest --target recover_data --tag files
