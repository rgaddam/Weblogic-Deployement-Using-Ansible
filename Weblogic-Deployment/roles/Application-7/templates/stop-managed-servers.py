# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Start editing mode
edit();
startEdit();

# Stop  Managed Server-1
stop('{{ managed_server_name-1 }}', block='false');

# Stop Managed Server-2
stop('{{ managed_server_name-2 }}', block='false');

# Disconnect from AdminServer
disconnect();
exit();
