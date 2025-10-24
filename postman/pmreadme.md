# Postman API Tests — System Info API

This folder contains Postman artifacts for testing the SRE Lab Demo FastAPI application.

## Contents
- `System_Info_API.postman_collection.json`: Collection of API endpoints and test cases.
- `environment.postman_environment.json`: Environment file defining base URL and variables.

## Usage
1. Import both files into Postman:
   - **File → Import → Upload Files**
   - Select both JSON files.

2. Set the active environment to **System Info API Env**.

3. Run all endpoints:
   - Open the **System Info API** collection.
   - Click **Run collection**.

4. Verify all tests pass (HTTP 200, valid JSON, correct structure).

## Automation (Optional)
You can run these same tests from the command line using [Newman](https://www.npmjs.com/package/newman):

```bash
npm install -g newman
newman run postman/System_Info_API.postman_collection.json \
  -e postman/environment.postman_environment.json

