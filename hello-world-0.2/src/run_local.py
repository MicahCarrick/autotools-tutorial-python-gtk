import os
from hello.application import Application

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

if __name__ == "__main__":
    app = Application(package="hello-world", 
                      package_name="Hello World",
                      version="0",
                      datadir=data_dir,
                      appdatadir=data_dir)
    app.run()
