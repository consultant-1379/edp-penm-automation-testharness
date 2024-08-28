mock_data={'svc_cluster': {'svc-1': 'testdata cloud-svc-1', 'svc-2': 'testdata cloud-svc-2', 'svc-3': 'testdata cloud-svc-3', 'svc-4': 'testdata cloud-svc-4', 'svc-5': 'testdata cloud-svc-5', 'svc-6': 'testdata cloud-svc-6'}, 'db_cluster': {u'db-1': 'testdata cloud-db-1', 'db-2': 'testdata cloud-db-2'}, 'scp_cluster': {'scp-1': 'testdata cloud-scp-1', 'scp-2': 'testdata cloud-scp-2', 'scp-3': 'testdata cloud-scp-3'}}

class LitpRestClient():
    def get_cluster_nodes(self):
      return mock_data
