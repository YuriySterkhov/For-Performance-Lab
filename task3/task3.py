def list_search(schedule):
   for i in range(len(values['values'])):
      for j in range(len(schedule)):
         if values['values'][i]['id'] == schedule[j]['id']:
            schedule[j]['value'] = values['values'][i]['value']
         if 'values' in schedule[j] and isinstance(schedule[j]['values'], list) == True:
            list_search(schedule[j]['values'])
import json
with open('tests.json', 'r') as f:
      tests = json.load(f)
with open('values.json', 'r') as f:
      values = json.load(f)
list_search(tests['tests'])
with open('report.json', 'w') as f:
   json.dump(tests, f, indent=2)
