FROM google/cloud-sdk:318.0.0-alpine

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN gcloud components install kubectl

ENTRYPOINT ["/entrypoint.sh"]
CMD ["info"]
