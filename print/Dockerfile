FROM camptocamp/mapfish_print:3.10.7
MAINTAINER Camptocamp "info@camptocamp.com"

RUN rm -rf webapps/ROOT/print-apps
COPY print-apps ${CATALINA_HOME}/webapps/ROOT/print-apps
COPY WEB-INF ${CATALINA_HOME}/webapps/ROOT/WEB-INF
ENV LOG_LEVEL DEBUG
