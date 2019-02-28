# AWS UTILS IMAGE

## Available commands

### `upload_tar`

Usage:
```bash
cat static_files.tar | docker run -i --rm  \
-e AWS_ACCESS_KEY=fake \
-e AWS_SECRET_KEY=fake \
-e UPLOAD_BUCKET=fake \
-e UPLOAD_PATH=fake \
 socialwifi/aws-utils upload_tar
```