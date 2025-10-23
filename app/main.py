from fastapi import FastAPI
import platform socket os subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SRE Lab Demo API running!"}

@app.get("/info")
def system_info():
    return {
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "release": platform.release(),
            "uptime": subprocess.getoutput("uptime -p")
            "container": os.environ.get("CONTAINER", "false")
    }
