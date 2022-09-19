#Task

But how we are going to now which todos belongs to user?

We are going to create a reference to the user in Todo model. This is called relation.

Do the following:
1. Add field `user_id` to the Todo model.
2. Change workflow a bit, now before we show all actions view, we should ask user to select existing user (lol), or create new.
3. Now you should use `user_id` while creating todo, also when you display list of todos, you should display only todos, that belongs to the current user.
4. Implement switching the users
5. You should store users data in `data.json` too!

Recording a demo is quite time-consuming so here you can launch example and see how it's working

Copy files from previous iteration
