# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Start editing mode
edit();
startEdit();

# Undeploy War files
print 'undeploying...'

# Undeploy Audit-portlet
undeploy('{{logout-theme}}', targets='{{cluster_server}}', timeout='40000'

disconnect()
exit()

