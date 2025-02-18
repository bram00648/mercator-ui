from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
print(f"FLASK_APP: {os.getenv('FLASK_APP')}")

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)




    # TODO: read context locals for testing
    