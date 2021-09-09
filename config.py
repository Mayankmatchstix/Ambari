Ambari configs.py - 

curl -H "X-Requested-By: ambari" -u admin "172.25.39.134:8080/api/v1/clusters/c4245/configurations/service_config_versions?service_name=KERBEROS”


/var/lib/ambari-server/resources/scripts/configs.py --host= 172.25.39.134 --port=8080 --user=admin --password='mayank.gupta' --cluster=c4245 --action=get--config-type=kerberos-env


/var/lib/ambari-server/resources/scripts/configs.py --user=admin --password=mayank.gupta --port=8080 --action=get --host=localhost --cluster=c4245 --config-type=kerberos-env


SSL - 

/var/lib/ambari-server/resources/scripts/configs.py --user=user --password=pass --port=8443 --protocol=https --action=get --host=localhost --cluster=clustername --config-type=kerberos-env --file=/tmp/kerberos.json

/var/lib/ambari-server/resources/scripts/configs.py --user=user --password=pass --port=8443 --protocol=https --action=set --host=localhost 
--cluster=clustername --config-type=spark2-env --file=/tmp/spark2-env_payload.json

https://community.cloudera.com/t5/Support-Questions/How-to-review-Kerberos-settings-In-Ambari/td-p/134721

https://community.cloudera.com/t5/Internal/How-to-update-modify-quot-ldap-url-quot-on-Ambari-gt/ta-p/276610

