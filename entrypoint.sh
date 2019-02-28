#!/bin/bash -e
mkdir -p ~/.aws/
cat >~/.aws/credentials <<_END
[default]
aws_access_key_id = $AWS_ACCESS_KEY
aws_secret_access_key = $AWS_SECRET_KEY
_END
exec $@
