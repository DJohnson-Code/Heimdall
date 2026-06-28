from dotenv import load_dotenv

load_dotenv()

from heimdall.pipeline.runner import run

if __name__ == "__main__":
    run()