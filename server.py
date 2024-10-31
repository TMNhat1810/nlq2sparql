from app import app
from app.configs import OPENAI_KEY

if __name__ == "__main__":
    print(OPENAI_KEY)
    app.run(host="0.0.0.0", port=5000)
