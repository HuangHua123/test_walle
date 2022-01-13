FROM python_flask:huanghua
LABEL maintainer="huanghua"

COPY ./* /data/test_walle/
WORKDIR /data/test_walle
EXPOSE 5014

CMD ["python3","test_walle.py"]