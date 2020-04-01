FROM mysql:5

ENV MYSQL_ROOT_PASSWORD 'root'

COPY ./init.sql/ /docker-entrypoint-initdb.d/

EXPOSE 3306