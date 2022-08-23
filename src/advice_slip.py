from requests import get


class AdviceSlip:
	def __init__(self):
		self.api = "https://api.adviceslip.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_advice(self):
		return get(
			f"{self.api}/advice"
			headers=self.headers).json()

	def get_advice_by_id(self, slip_id: int):
		return get(
			f"{self.api}/advice/{slip_id}"
			headers=self.headers).json()

	def search_advice(self, query: str):
		return get(
			f"{self.api}/advice/search/{query}",
			headers=self.headers).json()
