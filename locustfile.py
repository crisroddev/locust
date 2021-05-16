from locust import HttpUser, between, TaskSet

def index(l):
    l.client.get("/")

class UserBehaviour(TaskSet):
    tasks = { index: 1 }

class WebSiteUser(HttpUser):
    task_set = UserBehaviour
    wait_time = between(5.0, 9.0)
