import os
import time
import subprocess

import unittest

from selenium import webdriver

BASE_PROJECT_DIR = os.path.abspath(os.path.normpath('..'))
PYTHON_BINARY_NAME = "python" if os.name == "nt" else "python2"
TEST_SERVER_PORT = "7149"
FNULL = open(os.devnull, "w")


class TestTasksApp(unittest.TestCase):

    def setUp(self):
        self.main_page = os.path.join(BASE_PROJECT_DIR, "index.html")

        self.server_args = [PYTHON_BINARY_NAME, "-m", "SimpleHTTPServer", TEST_SERVER_PORT]

        self.browser = webdriver.Chrome()

        self.server_process = subprocess.Popen(self.server_args, cwd=BASE_PROJECT_DIR, stdout=FNULL, stderr=FNULL)

    def open_main_page(self):
        # self.browser.get('file://' + self.main_page)
        self.browser.get('localhost:{port}'.format(port=TEST_SERVER_PORT))
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()
        self.server_process.terminate()

    def get_create_task_btn(self):
        return self.browser.find_element_by_css_selector('button#create-task-btn')

    def add_list_entry(self, text_input, submit_btn, todo_text):
        text_input.send_keys(todo_text)
        submit_btn.click()

    def get_list_entry_count(self):
        list_entries = self.browser.find_elements_by_class_name('task-entry')
        return len(list_entries)

    def test_page_has_proper_title(self):
        self.open_main_page()
        self.assertIn("AskItTask", self.browser.title)

    def test_tasks_correctly_submitted(self):
        self.open_main_page()

        submit_task_btn = self.get_create_task_btn()
        text_input = self.browser.find_element_by_class_name('todo-input-text')

        self.add_list_entry(text_input, submit_task_btn, 'New Task 1')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 2')

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        self.assertEqual(len(list_entries), 2)
        self.assertEqual(list_entries[0].text, 'New Task 1')

    def test_tasks_submited_on_ENTER_key(self):
        self.open_main_page()

        entries_number_before_submit = self.get_list_entry_count()

        text_input = self.browser.find_element_by_class_name('todo-input-text')
        text_input.send_keys('New Task 1' + '\n')

        entries_number_after_submit = self.get_list_entry_count()
        self.assertEqual(entries_number_after_submit, entries_number_before_submit + 1, msg="Element was not added on enter key press")

    def test_delete_tasks_correctly(self):
        self.open_main_page()

        text_input = self.browser.find_element_by_class_name('todo-input-text')

        submit_task_btn = self.browser.find_element_by_css_selector('button#create-task-btn')

        entries_number_before_submit = self.get_list_entry_count()

        self.add_list_entry(text_input, submit_task_btn, 'New Task 1')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 2')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 3')
        self.add_list_entry(text_input, submit_task_btn, 'New Task 4')

        delete_third_btn = self.browser.find_elements_by_css_selector('span.glyphicon.glyphicon-trash')[entries_number_before_submit + 2]
        delete_third_btn.click()

        # Task dissapear with animation, so we have to wait a bit
        time.sleep(1)

        list_entries = self.browser.find_elements_by_class_name('task-entry')
        new_todos_texts = [x.text for x in list_entries]

        entries_number_after_submit = self.get_list_entry_count()

        self.assertEqual(entries_number_after_submit, entries_number_before_submit + 3, msg="Element was not deleted.")
        self.assertEqual(new_todos_texts[entries_number_before_submit:], ['New Task 1', 'New Task 2', 'New Task 4'])

    def test_empty_task_not_submited(self):
        self.open_main_page()

        submit_task_btn = self.get_create_task_btn()

        list_entries_before = self.browser.find_elements_by_class_name('task-entry')
        entries_count_before_submit = len(list_entries_before)

        text_input = self.browser.find_element_by_class_name('todo-input-text')

        self.add_list_entry(text_input, submit_task_btn, '')

        list_entries = self.browser.find_elements_by_class_name('task-entry')

        self.assertEqual(len(list_entries), entries_count_before_submit, msg="Empty element added to the list.")

    def test_submitting_empty_TODO_by_clicking_button_shows_error(self):
        self.open_main_page()

        submit_task_btn = self.get_create_task_btn()
        text_input = self.browser.find_element_by_class_name('todo-input-text')
        self.add_list_entry(text_input, submit_task_btn, '')

        alert_div = self.browser.find_element_by_id('alertEmptyField')
        self.assertIn("To-do content can not be empty", alert_div.text)

    def test_submitting_empty_TODO_by_pressing_ENTER_button_shows_error(self):
        self.open_main_page()

        text_input = self.browser.find_element_by_class_name('todo-input-text')
        text_input.send_keys('\n')

        alert_div = self.browser.find_element_by_id('alertEmptyField')
        self.assertIn("To-do content can not be empty", alert_div.text)

if __name__ == '__main__':
    unittest.main()
