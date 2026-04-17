FROM waron97/testrunner

USER root

RUN apt-get update && apt-get install -y git openssh-client rsync && rm -rf /var/lib/apt/lists/*
RUN pip3 install redis requests flask

RUN mkdir -p /home/odoo/.ssh
COPY ./ssh-key /home/odoo/.ssh/id_rsa
RUN chmod 600 /home/odoo/.ssh/id_rsa \
    && chown -R odoo:odoo /home/odoo/.ssh \
    && ssh-keyscan ssh.dev.azure.com >> /home/odoo/.ssh/known_hosts 2>/dev/null \
    && ssh-keyscan github.com >> /home/odoo/.ssh/known_hosts 2>/dev/null

COPY ./startup.sh /opt/startup.sh
COPY ./orchestrator.py /opt/orchestrator.py
RUN mkdir -p /opt/repo /results \
    && chmod +x /opt/startup.sh \
    && chown odoo:odoo /opt/startup.sh /opt/orchestrator.py /opt/repo /results \
    && chown -R odoo:odoo /opt/odoo/addons

USER odoo
ENTRYPOINT ["/opt/startup.sh"]
