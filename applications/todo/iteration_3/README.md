# Task

This will be a small one.

I've created new file `types.py` and added dataclasses to represent our Todos and Actions.

Now use Todo dataclass everywhere instead of dicts.

I already updated `DATA` variable, you can copy other functions
from previous iteration and adjust them

Use Action dataclass to represent actions.

Use `ACTIONS` (first add needed actions there) list to create action choices

As you might have noticed, you have some parts where user need to choice (todo or action). Make function that will handle selecting an item from any list. (look at `select_item` function in the main file)

For `select_item` you will need to print 2 types of objects (Todo & Action).
It's recommended to allow this classes to handle how they are displayed on their own
(you need to find out how to change what objects returns when `str` method called).

To do this you can use `id` attribute,
so don't stick to the demo to strictly for this.

Also you can add any other functions, so try to find out some other upgrades

Check example folder to see my implementation of this iteration
