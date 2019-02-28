FROM python:3.6-alpine
COPY entrypoint.sh /opt/
COPY cloud_test_app /opt/cloud_test_app
COPY etc/conf.py /etc/cloud_test/
RUN apk add --no-cache \
      bash \
      gcc \
      curl \
      g++ \
      libstdc++ \
      linux-headers \
      musl-dev \
      postgresql-dev \
      mariadb-dev;

# install django app requirements and gunicorn
RUN pip install --trusted-host pypi.python.org -r opt/cloud_test_app/requirements.txt
RUN pip install gunicorn

EXPOSE 8000
WORKDIR /opt

# set entrypoint and command (see entrypoint.sh)
ENTRYPOINT ["/opt/entrypoint.sh"]  # Use entrypoint script
CMD ["--start-service"]  # Default parameters to start the service
