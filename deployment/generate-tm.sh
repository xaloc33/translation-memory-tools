#!/bin/bash

ROOT="$1"
PROGRAMS=$ROOT/tm-git/src
BUILDER=$PROGRAMS
PROJECTS=$ROOT/tm-git/cfg/projects
NEW_POS=$PROGRAMS/output

copy_tm_files() {

    cd $NEW_POS
    # Copy only new PO files
    for filename in $1; do
        # If file exists and size is greater than 200 bytes
        if [ -e  "$filename" ]; then
            fsize=$(du -b "$filename" | cut -f 1)
            if [ $fsize -ge $2 ]; then
                if ! diff -q "$filename" "$3/$filename" > /dev/null; then
                    echo "Copying $filename"
                    cp "$filename" "$3/$filename"
                fi
            fi
        fi
    done
}

if [ "$#" -ne 1 ] ; then
    echo "Usage: generate-tm.sh ROOT_DIRECTORY_OF_BUILD_LOCATION"
    echo "Invalid number of parameters"
    exit
fi 

INTERMEDIATE_PO=$ROOT/translation-memories/po
INTERMEDIATE_TMX=$ROOT/translation-memories/tmx
BACKUP_DIR=$ROOT/previous

# Catalan locale does not support thousand separator
export LC_ALL=ast_ES.utf-8

# Copy existing PO files
rm -r -f $BACKUP_DIR
mkdir $BACKUP_DIR
cd $BACKUP_DIR
cp $INTERMEDIATE_PO/* $BACKUP_DIR

# Build new translation files
cd $BUILDER
rm -f *.log
rm -f -r $NEW_POS

# Download new translation files
python builder.py -d
python builder.py --all
python builder.py --softcatala

copy_tm_files "*.po" 200 $INTERMEDIATE_PO

# Empty TMX files are 275 bytes (just the header)
# Files with one short translation 450 bytes       
copy_tm_files "*.tmx" 350 $INTERMEDIATE_TMX

# Update download file & index
cd $PROGRAMS
python download-creation.py -d $INTERMEDIATE_PO -t $INTERMEDIATE_TMX
python index-creation.py -d $NEW_POS
