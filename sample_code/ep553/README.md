# [debugging a sentry test pollution! (intermediate)](https://youtu.be/YEIeKdBmuUY)

Today I show off how to use my `detect-test-pollution` tool -- I also showed a neat debugging technique to help me figure out what was actually breaking the test!

## Interactive examples

### Python

```python
class WtfDict(dict):
    def __delitem__(self, k):
        breakpoint()
        return super().__delitem__(k)
```

### Python debugger (pdb)

```
where
q
```

### Bash

```bash
git clone --depth=1 git@github.com:getsentry/sentry
cd sentry/

pytest tests/sentry/integrations/slack/test_tasks.py::SlackTasksTest::test_task_existing_rule
pytest tests/sentry/integrations/slack/test_tasks.py

detect-test-pollution --tests tests/sentry/integrations/slack/test_tasks.py --failing-test tests/sentry/integrations/slack/test_tasks.py::SlackTasksTest::test_task_existing_rule

pytest tests/sentry/integrations/slack/test_tasks.py::SlackTasksTest__InRegionMode::test_post_message_failure tests/sentry/integrations/slack/test_tasks.py::SlackTasksTest::test_task_existing_rule
nano src/sentry/api/endpoints/project_rules.py
```
