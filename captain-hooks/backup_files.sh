#!/usr/bin/bash
# restic -r b2:edwh-backup-test:backup-testapplication init

#Voer hier backup programma's in voor intern in de docker, let aan goede volumes in de docker-compose!

source __tinkerbell__.sh

echorun restic $HOST -r $URI backup ./backups --tag files

rm -r ./backups/*
