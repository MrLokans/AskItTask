import os

import unittest

from selenium import webdriver

BASE_PROJECT_DIR = os.path.abspath(os.path.normpath('..'))


class TestTasksApp(unittest.TestCase):

    def setUp(self):
        self.main_page = os.path.join(BASE_PROJECT_DIR, "index.html")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def open_main_page(self):
        self.browser.get('file://' + self.main_page)

    def tearDown(self):
        self.browser.quit()

    def test_page_has_proper_title(self):
        self.open_main_page()
        self.assertIn("AskItTask", self.browser.title)

    def test_tasks_correctly_submitted(self):
        self.open_main_page()
        create_task_btn = self.browser.find_element_by_id('create-task-btn')
        create_task_btn.click()

        submit_task_btn = self.browser.find_element_by_css_selector('button#createTask')
        text_input = self.browser.find_element_by_class_name('todo-input-text')
        text_input.send_keys('New Task 1')
        submit_task_btn.click()

        text_input.send_keys('New Task 2')
        submit_task_btn.click()

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        self.assertEqual(len(list_entries), 2)
        self.assertEqual(list_entries[0].text, 'New Task 1')

    def test_tasks_submited_on_ENTER_key(self):
        self.open_main_page()
        create_task_btn = self.browser.find_element_by_id('create-task-btn')
        create_task_btn.click()

        list_entries_before = self.browser.find_elements_by_class_name('task-entry')
        entries_count_before_submit = len(list_entries_before)

        text_input = self.browser.find_element_by_class_name('todo-input-text')
        text_input.send_keys('New Task 1' + '\n')

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        self.assertEqual(len(list_entries), entries_count_before_submit + 1, msg="Element was not added on enter key press")

    def test_delete_tasks_correctly(self):
        self.open_main_page()
        create_task_btn = self.browser.find_element_by_id('create-task-btn')
        create_task_btn.click()

        text_input = self.browser.find_element_by_class_name('todo-input-text')

        submit_task_btn = self.browser.find_element_by_css_selector('button#createTask')

        text_input.send_keys('New Task 1')
        submit_task_btn.click()

        text_input.send_keys('New Task 2')
        submit_task_btn.click()

        text_input.send_keys('New Task 3')
        submit_task_btn.click()

        text_input.send_keys('New Task 4')
        submit_task_btn.click()

        delete_third_btn = self.browser.find_elements_by_css_selector('span.glyphicon.glyphicon-trash')[2]
        delete_third_btn.click()

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        list_entries = [x.text for x in list_entries]
        self.assertEqual(len(list_entries), 3)
        # self.assertEqual(list_entries, ['New Task 1', 'New Task 2', 'New Task 4'])


if __name__ == '__main__':
    unittest.main()
