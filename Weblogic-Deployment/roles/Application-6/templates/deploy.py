# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Start editing mode
edit();
startEdit();

# Deploy new war files
print 'deploying...'

# # Deploy Base-theme-war & Start Application
deploy('{{liferay-portal-6.2-ee-sp14}}', '/apps/oracle/domains/applications/{{liferay-portal-6.2-ee-sp14}}', targets='{{cluster_server}}'
startApplication('liferay-portal-6.2-ee-sp14')

# Deployment Completed
print 'Deployment completed successfully'

disconnect()
exit()
