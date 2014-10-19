from base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

# Student arrives at qbank website and notices how nice it looks awesome
	def test_layout_and_styling(self):
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		inputbox = self.browser.find_element_by_id('submit_id')
		self.assertAlmostEqual(
			inputbox.size['width'], 224, delta=5
			)

		self.assertIn('Neurosurgery', self.browser.title)