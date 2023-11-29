from locust import HttpUser, task, between

class CandidateUser(HttpUser):
    wait_time = between(3, 6)

    @task
    def test_taker(self):
        #self.client.get("/tests-qry")
        self.client.get("//tests-taker/init/3/13")
        # self.client.get("http://abcjobs-public-alb-388103681.us-east-1.elb.amazonaws.com/tests-qry")
