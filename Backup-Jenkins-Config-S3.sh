#!/usr/bin/env bash

# Generate timestamped filename
TIMESTAMPED_TAG=`date +%Y-%m-%d-%H%M%S`
BACKUP_ARCHIVE="./jenkins-backup-${TIMESTAMPED_TAG}.tar.gz"

# Inconceivable race condition avoidance
if [-f $BACKUP_ARCHIVE ]; then
	rm ${BACKUP_ARCHIVE}
fi

# Archive everything on jenkins but workspace, .file, .folders and m2 files, whatever these are
# If the jenkins folder changes half way through, tar will fail; retry up to 5 times
COUNTER=0
until [ $COUNTER -ge 5 ]
do
    tar -czvf ${BACKUP_ARCHIVE} --exclude="workspace" --exclude=".m2" --exclude=builds --exclude=".*" /var/lib/jenkins && break
    
    # If we get here, tar failed!
    echo "Archive creation failed, retrying..."
    COUNTER=$[$COUNTER+1]
    sleep 15
done

# Place on s3 and cleanup
aws s3 cp ${BACKUP_ARCHIVE} s3://${S3_BUCKET}/jenkins-backups/
rm ${BACKUP_ARCHIVE}
