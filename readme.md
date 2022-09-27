# Login Auth

## Usage

1. Run the python program file
2. Set your username and password
3. Input your username and password if you want, or quit the program as your username and password's `md5` value has been saved locally
4. If you want to login the next time, run the program directly and input your username and password

## Technical Details

### Username and password saving

The save of username and password use `md5`, as it's a mad safe way to store your data. Nobody can access your password or username from the `md5` value.

So why can the program compare the input password with the stored `md5` value? Because it can generate the `md5` value of the input password and compare the `hash` of `md5` values.

### Run requirements

Please run using `python3`.
