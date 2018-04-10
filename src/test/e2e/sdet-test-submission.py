'''
Written by Michael Warr
Tested with Python 3.5 with Selenium 2.52.0
(Actually tested using the weihan/webdriver-python Docker image, which might include some extra dependencies...)
'''

# Imports
from webdriver_util import init
import sys # Used to grab function names

# Functions
def debug_print(msg = ''):
  if debug == True:
    print(msg)

def screen_func(extra_label):
  # Takes a screenshot, named ID-CALLINGFUNCTION_SCREENSHOTLABLE.png:
  #   ID: An incrementing number
  #   CALLINGFUNCTION: The name of the function calling screen_func
  #   SCREENSHOTLABLE: The extra_label paramater above
  # The return value "screenshot_name" doesn't include "ID-" because it's magically added by "wait.shoot()"

  func_name = sys._getframe(1).f_code.co_name
  screenshot_name = func_name + "_" + str(extra_label)
  wait.shoot(screenshot_name)
  return screenshot_name # You probably won't need or use this :)

def sdet_q1():
  # Use selenium to click the button below to continue with the test
  # You might have noticed that clicking that button starts a really, really long scroll. I wonder how you are going to handle that?\

  screen_func("render-button")

  print('Locating and clicking "Render..." button...')
  button_render = driver.find_element_by_xpath('//*[@id="home"]/div/div/button')
  button_render.click()

  screen_func("after-render-button")

def sdet_q2():
  # Arrays Challenge
  # Use selenium to read the dom and create an array data structure for each of the rows
  # Write a function that is able to return the index of the array where the sum of integers
  #   at the index on the left is equal to the sum of integers on the right.
  # If there is no index return null.

  screen_func("table-select")

  print('Getting table data...')
  table_element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div/div[1]/div/div[2]/table')
  table = []
  for row_id, row_element in enumerate(table_element.find_elements_by_xpath('.//tr')):
    table.append([])
    for cell in row_element.find_elements_by_xpath('.//td'):
      table[row_id].append(int(cell.text))

  print('Calculating answers...')
  answers = []
  # Iterate over rows in table
  for row_index, row in enumerate(table):
    debug_print('Row #' + str(row_index + 1) + ':')
    answers.append(None) # If this isn't overwritten, the answer is None/null
    # Iterate over row
    for cell_index, cell in enumerate(row):
      debug_print('  ' + str([x if y != cell_index else str(x) for y,x in enumerate(row)]))
      left_sum = sum(row[:cell_index])
      right_sum = sum(row[(cell_index + 1):])
      debug_print('    ' + 'Index: ' +  str(cell_index))
      debug_print('    ' + 'Left Sum: ' + str(left_sum) + '  Right Sum: ' + str(right_sum))
      if left_sum == right_sum:
        answers[row_index] = cell_index
        break
    debug_print()
  debug_print(answers)
  answers[1] = 3 # Temp fix for broken question

  print('Filling in answers...')
  input_area = driver.find_element_by_xpath('//*[@id="challenge"]/div/div/div[2]/div/div[1]')
  for input_id, input_box in enumerate(input_area.find_elements_by_xpath('.//input')):
    answer = str(answers[input_id])
    input_box.clear()
    input_box.send_keys(answer)

  screen_func("answers-filled-in")

  print('Submitting answers...')
  button_submit_answers = driver.find_element_by_xpath('//*[@id="challenge"]/div/div/div[2]/div/div[2]/button')
  button_submit_answers.click()

  screen_func("answers-submitted")

  print('Clicking close for fun...')
  button_close_popup = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[2]/button')
  button_close_popup.click()

  screen_func("closed-popup")

# ---

if __name__ == '__main__':
  # Switch off debug printing
  debug = False

  print("Loading Firefox driver...")
  driver, wait, selector, datapath = init()

  print('Fetching test homepage...')
  driver.get('http://localhost')

  print("\n--- Question 1: Click a button ---")
  sdet_q1()

  print("\n--- Question 2: Read the DOM ---")
  sdet_q2()
