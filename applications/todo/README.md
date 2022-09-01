# TODO App

### What is TODO App?

TODO app is an application to note/track things you want to do.

### Features required

1. See list of your todo's  (List)
2. Add todo
3. See separate todo
4. Update todo (e.g. mark as done)
5. Delete todo

This is so-called CRUD (Create, Read, Update, Delete)

### Extra features

1. Saving data between program launches
2. Be able to handle multiple users, each can save it own todos


### Testing

To run test you need to be in this directory and call

```shell
python -m unittest iteration_*/test.py
```

Tests are very simple, it's checks just normal flow,
to see inputs that your code will receive you can check
`test_utils.py` and it's `FLOW_INPUTS` variables
