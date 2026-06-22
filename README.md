# Load Testing Suite 📈

Load testing with k6 and Locust, integrated with Grafana.

## Tools

| Tool | Use Case |
|------|----------|
| k6 | API load testing |
| Locust | Distributed testing |
| Grafana | Real-time dashboards |

## Quick Start

```bash
k6 run tests/api-load.js
locust -f locustfile.py --host=https://api.example.com
```

## License

MIT