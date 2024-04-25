For running this go inside aap using cd app,
then install the requirement thereafter run on local host using  python manage.py runserver


for question 1:
import re

text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

numbers = re.findall(r'(?<="id":\s*)(\d+)', text)

print(numbers)


for question 3:
B. Use Flask for lightweight applications with minimal boilerplate, ideal for small-scale projects or APIs. Django is preferable for complex applications requiring built-in features like ORM, admin interface, and authentication, suitable for large-scale projects with comprehensive requirements.
