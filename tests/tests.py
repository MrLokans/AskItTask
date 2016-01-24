import os
import time

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

    def add_list_entry(self, text_input, submit_btn, todo_text):
        text_input.send_keys(todo_text)
        submit_btn.click()

    def test_page_has_proper_title(self):
        self.open_main_page()
        self.assertIn("AskItTask", self.browser.title)

    def test_tasks_correctly_submitted(self):
        self.open_main_page()

        submit_task_btn = self.browser.find_element_by_css_selector('button#createTask')
        text_input = self.browser.find_element_by_class_name('todo-input-text')

        self.add_list_entry(text_input, submit_task_btn, 'New Task 1')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 2')

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        self.assertEqual(len(list_entries), 2)
        self.assertEqual(list_entries[0].text, 'New Task 1')

    def test_tasks_submited_on_ENTER_key(self):
        self.open_main_page()

        list_entries_before = self.browser.find_elements_by_class_name('task-entry')
        entries_count_before_submit = len(list_entries_before)

        text_input = self.browser.find_element_by_class_name('todo-input-text')
        text_input.send_keys('New Task 1' + '\n')

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        self.assertEqual(len(list_entries), entries_count_before_submit + 1, msg="Element was not added on enter key press")

    def test_delete_tasks_correctly(self):
        self.open_main_page()

        text_input = self.browser.find_element_by_class_name('todo-input-text')

        submit_task_btn = self.browser.find_element_by_css_selector('button#createTask')

        self.add_list_entry(text_input, submit_task_btn, 'New Task 1')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 2')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 3')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 4')

        delete_third_btn = self.browser.find_elements_by_css_selector('span.glyphicon.glyphicon-trash')[2]
        delete_third_btn.click()

        # Task dissapear with animation, so we have to wait a bit
        time.sleep(1)

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        list_entries = [x.text for x in list_entries]
        self.assertEqual(len(list_entries), 3, msg="Element was not deleted.")
        # self.assertEqual(list_entries, ['New Task 1', 'New Task 2', 'New Task 4'])

    def test_empty_task_not_submited(self):
        self.open_main_page()

        submit_task_btn = self.browser.find_element_by_css_selector('button#createTask')

        list_entries_before = self.browser.find_elements_by_class_name('task-entry')
        entries_count_before_submit = len(list_entries_before)

        text_input = self.browser.find_element_by_class_name('todo-input-text')

        self.add_list_entry(text_input, submit_task_btn, '')

        list_entries = self.browser.find_elements_by_class_name('task-entry')

        self.assertEqual(len(list_entries), entries_count_before_submit, msg="Empty element added to the list.")


if __name__ == '__main__':
    unittest.main()
