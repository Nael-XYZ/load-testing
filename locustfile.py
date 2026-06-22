from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def health_check(self):
        self.client.get("/health")
        
    @task(3)
    def get_data(self):
        self.client.get("/api/data")
