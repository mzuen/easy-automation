import requests


class TestApiBinOrg:

    api_host = "https://httpbin.org"

    def get(self, url, params={}):
        resp = requests.get(url=url, params=params)
        return resp

    def test_get_api(self):
        path = "/get"
        api_endpoint = self.api_host + path
        expected_result = {"url": "https://httpbin.org/get"}

        resp_obj = self.get(url=api_endpoint)
        resp_json = resp_obj.json()
        assert isinstance(resp_json, dict)
        assert resp_json['url'] == expected_result["url"]
    
    def test_get_api_args(self):
        path = "/get"
        api_endpoint = self.api_host + path
        args = {"hello": "pytest"}
        
        expected_result = {"url": "https://httpbin.org/get", "args": args}

        resp_obj = self.get(url=api_endpoint, params=args)
        resp_json = resp_obj.json()
        assert isinstance(resp_json, dict)
        assert resp_json['args'] == expected_result["args"]
    
