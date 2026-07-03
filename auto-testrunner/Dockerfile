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
COPY ./config.py /opt/config.py
COPY ./ado.py /opt/ado.py
COPY ./runner.py /opt/runner.py
COPY ./notifier.py /opt/notifier.py
COPY ./poller.py /opt/poller.py
COPY ./api.py /opt/api.py
COPY ./orchestrator.py /opt/orchestrator.py
COPY ./base_db.py /opt/base_db.py
COPY ./upgrade.py /opt/upgrade.py
RUN mkdir -p /opt/repo /results \
    && chmod +x /opt/startup.sh \
    && chown odoo:odoo /opt/startup.sh /opt/config.py /opt/ado.py /opt/runner.py \
                       /opt/notifier.py /opt/poller.py /opt/api.py /opt/orchestrator.py \
                       /opt/base_db.py /opt/upgrade.py \
                       /opt/repo /results \
    && chown -R odoo:odoo /opt/odoo/addons

USER odoo
ENTRYPOINT ["/opt/startup.sh"]
