FROM mysql:8.0
ENV MYSQL_ROOT_PASSWORD=admin123
ADD dbinit.sql /docker-entrypoint-initdb.d
EXPOSE 3306

