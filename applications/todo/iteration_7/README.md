#Task

Now it's time for refactoring!

You will work with code from example from previous iteration

I won't describe all the details but give you main vectors to work on. And also show my example.

Main vectors are:
1. All functions are in 1 file, try to group them to separate files
2. Our models (`Todo` `User`) contains same methods (`from_json` `tod_dict`) create class `BaseModel` which will contain these methods, and make our models inherit it.
3. Add function to calculate id for new item regardless of model (should take model's key in DATA as input)
4. If you've nice functions split, you should notice that you are using only few of each file, mark with underscore e.g. `_func_name` to mark them as "private". Private means other modules shouldn't import and use this functions
5. Think about how you can adjust flow control in main file, using actions ids isn't a great way to do this.
