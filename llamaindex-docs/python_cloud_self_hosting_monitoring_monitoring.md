[Skip to content](https://developers.llamaindex.ai/python/cloud/self_hosting/monitoring/monitoring/#_top)
# Monitoring
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
##  Self-Hosting Documentation Access 
This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more. 
Self-Hosting Documentation Access Granted  Logout 
LlamaCloud services expose metrics, which are collected by [Prometheus](https://prometheus.io) and visualized in [Grafana](https://grafana.com).
## Prerequisites
[Section titled “Prerequisites”](https://developers.llamaindex.ai/python/cloud/self_hosting/monitoring/monitoring/#prerequisites)
To monitor your LlamaCloud deployment, you’ll need:
  * [Prometheus](https://prometheus.io) - For metrics collection and storage
  * [Grafana](https://grafana.com) - For metrics visualization
  * [AlertManager](https://prometheus.io/docs/alerting/latest/alertmanager/) - For alert management


These services can be deployed using the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) Helm chart, which provides a complete monitoring solution that includes:
  * Prometheus server for metrics collection
  * Grafana for visualization with pre-configured dashboards
  * AlertManager for handling alerts
  * Node exporter for hardware and OS metrics
  * kube-state-metrics for Kubernetes object metrics
  * Prometheus Operator for managing Prometheus instances


Use this file as a starting point for a basic installation:
kube-prometheus-stack.yaml```


prometheus:




enabled: true




grafana:




enabled: true




alertmanager:




enabled: true


```

Terminal window```


helmrepoaddprometheus-communityhttps://prometheus-community.github.io/helm-charts




helmrepoupdate




helminstallkube-prometheus-stackprometheus-community/kube-prometheus-stack\




-fkube-prometheus-stack.yaml


```

For more information about the kube-prometheus-stack Helm chart, please refer to the [kube-prometheus-stack README](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack).
## Service Monitoring
[Section titled “Service Monitoring”](https://developers.llamaindex.ai/python/cloud/self_hosting/monitoring/monitoring/#service-monitoring)
After installing the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) Helm chart, you should create `ServiceMonitor` objects. These objects tell Prometheus to scrape the metric endpoints exposed by the LlamaCloud services.


```


apiVersion: monitoring.coreos.com/v1




kind: ServiceMonitor




metadata:




# 👇 The name of the service you want to monitor.




name: llamacloud




# 👇 The namespace where the ServiceMonitor object lives; typically the namespace where you installed the chart.




namespace: <kube-prometheus-stack-namespace>




labels:




# 👇 Typically this is the same namespace as above.




release: kube-prometheus-stack




spec:




namespaceSelector:




matchNames:




# 👇 The namespace you installed Llamacloud into.




- <llamacloud-namespace>




selector:




matchLabels:




app.kubernetes.io/instance: llamacloud




app.kubernetes.io/name: llamacloud




app.kubernetes.io/managed-by: Helm




endpoints:




- port: http




path: /metrics




interval: 30s




scrapeTimeout: 10s


```

```


apiVersion: monitoring.coreos.com/v1




kind: ServiceMonitor




metadata:




# 👇 The name of the service you want to monitor.




name: llamacloud-operator




# 👇 The namespace where the ServiceMonitor object lives; typically the namespace where you installed the chart.




namespace: <kube-prometheus-stack-namespace>




labels:




# 👇 Typically this is the same namespace as above.




release: kube-prometheus-stack




spec:




namespaceSelector:




matchNames:




# 👇 The namespace you installed Llamacloud into.




- <llamacloud-namespace>




selector:




matchLabels:




app.kubernetes.io/instance: llamacloud




app.kubernetes.io/name: llamacloud-operator




app.kubernetes.io/managed-by: Helm




endpoints:




- port: http




path: /metrics




interval: 30s




scrapeTimeout: 10s


```

```


apiVersion: monitoring.coreos.com/v1




kind: ServiceMonitor




metadata:




# 👇 The name of the service you want to monitor.




name: llamacloud-worker




# 👇 The namespace where the ServiceMonitor object lives; typically the namespace where you installed the chart.




namespace: <kube-prometheus-stack-namespace>




labels:




# 👇 Typically this is the same namespace as above.




release: kube-prometheus-stack




spec:




namespaceSelector:




matchNames:




# 👇 The namespace you installed Llamacloud into.




- <llamacloud-namespace>




selector:




matchLabels:




app.kubernetes.io/instance: llamacloud




app.kubernetes.io/name: llamacloud-worker




app.kubernetes.io/managed-by: Helm




endpoints:




- port: http




path: /metrics




interval: 30s




scrapeTimeout: 10s


```

```


apiVersion: monitoring.coreos.com/v1




kind: ServiceMonitor




metadata:




# 👇 The name of the service you want to monitor.




name: llamacloud-parse




# 👇 The namespace where the ServiceMonitor object lives; typically the namespace where you installed the chart.




namespace: <kube-prometheus-stack-namespace>




labels:




# 👇 Typically this is the same namespace as above.




release: kube-prometheus-stack




spec:




namespaceSelector:




matchNames:




# 👇 The namespace you installed Llamacloud into.




- <llamacloud-namespace>




selector:




matchLabels:




app.kubernetes.io/instance: llamacloud




app.kubernetes.io/name: llamacloud-parse




app.kubernetes.io/managed-by: Helm




endpoints:




- port: http




path: /metrics




interval: 30s




scrapeTimeout: 10s


```

```


apiVersion: monitoring.coreos.com/v1




kind: ServiceMonitor




metadata:




# 👇 The name of the service you want to monitor.




name: llamacloud-ocr




# 👇 The namespace where the ServiceMonitor object lives; typically the namespace where you installed the chart.




namespace: <kube-prometheus-stack-namespace>




labels:




# 👇 Typically this is the same namespace as above.




release: kube-prometheus-stack




spec:




namespaceSelector:




matchNames:




# 👇 The namespace you installed Llamacloud into.




- <llamacloud-namespace>




selector:




matchLabels:




app.kubernetes.io/instance: llamacloud




app.kubernetes.io/name: llamacloud-ocr




app.kubernetes.io/managed-by: Helm




endpoints:




- port: http




path: /metrics




interval: 30s




scrapeTimeout: 10s


```

## Grafana
[Section titled “Grafana”](https://developers.llamaindex.ai/python/cloud/self_hosting/monitoring/monitoring/#grafana)
Once you have installed the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) and installed the `ServiceMonitor` objects into your Kubernetes cluster, you will be able to view the metrics in Grafana.
First, get the Grafana `admin` user’s password:
Terminal window```


kubectl--namespace<llamacloud-namespace>getsecretskube-prometheus-stack-grafana-ojsonpath="{.data.admin-password}"|base64-decho


```

Next, create a `port-forward` to Grafana:
Terminal window```


exportGRAFANA_POD_NAME=$(kubectl--namespace<llamacloud-namespace>\




getpod-l"app.kubernetes.io/name=grafana,app.kubernetes.io/instance=kube-prometheus-stack"-oname)




kubectl--namespace<llamacloud-namespace>port-forward$GRAFANA_POD_NAME3000


```

Now open your browswer to `localhost:3000` and log into the Grafana console. You should be able to explore all the LlamaCloud metrics in the **Explore** tab.
