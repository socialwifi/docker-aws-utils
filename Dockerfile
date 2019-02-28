FROM socialwifi/kubeyard-python:3.7.0-0
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
