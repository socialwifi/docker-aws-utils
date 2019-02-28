import io
import mimetypes
import pathlib
import sys
import tarfile

import boto3
from aws_utils import settings


def run():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.UPLOAD_BUCKET)
    tar = tarfile.open(mode='r|', fileobj=sys.stdin.buffer)
    for tarinfo in tar:
        if tarinfo.isfile():
            with tar.extractfile(tarinfo) as data_stream:
                bytes = io.BytesIO(data_stream.read())
            kwargs = {
                'Key': str(pathlib.PurePosixPath(settings.UPLOAD_PATH) / tarinfo.path),
                'Body': bytes,
            }
            mime_type, _ = mimetypes.guess_type(tarinfo.path)
            if mime_type:
                kwargs['ContentType'] = mime_type
            bucket.put_object(**kwargs)
    tar.close()


if __name__ == '__main__':
    exit(run())
