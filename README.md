
# Clinical Trial Data Pipeline

This project is a Python-based ETL (Extract, Transform, Load) pipeline for retrieving, transforming, and storing clinical trial data from clinicaltrials.gov into a MongoDB database.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
  - [3. Install and Start MongoDB](#3-install-and-start-mongodb)
  - [4. Set Environment Variables (Optional)](#4-set-environment-variables-optional)
  - [5. Run the Pipeline](#5-run-the-pipeline)
- [Verify Data in MongoDB](#verify-data-in-mongodb)
- [Future Improvements](#future-improvements)

---

## Project Overview

This pipeline retrieves clinical trials data updated between specified dates from clinicaltrials.gov, maps it to a structured JSON format, and stores it in a MongoDB collection. It also extracts disease-related information from the `eligibilityCriteria` field using keyword matching.

---

## Requirements

- **Python** 3.8 or higher
- **MongoDB** (local installation or Docker setup)
- **Node.js and npm** (optional if there are Node dependencies)

---

## Setup

### 1. Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url> && cd project
```

> Replace `<repository-url>` with the actual GitHub URL of this repository.

### 2. Install Dependencies

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

If you are using Node.js in your project, install Node dependencies as well:

```bash
npm install
```

### 3. Install and Start MongoDB

#### Option A: Install MongoDB Locally

1. **Download MongoDB Community Edition** from [MongoDB's official download page](https://www.mongodb.com/try/download/community).
2. Follow the installation instructions for your operating system.
3. Start MongoDB:
   - **Windows**: Open Command Prompt or PowerShell and run:
     ```bash
     "C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe"
     ```
   - **macOS** (with Homebrew):
     ```bash
     brew tap mongodb/brew
     brew install mongodb-community
     brew services start mongodb/brew/mongodb-community
     ```
   - **Linux**:
     ```bash
     sudo systemctl start mongod
     ```

#### Option B: Run MongoDB with Docker

If you have Docker installed, you can run MongoDB as a container:

```bash
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

This will make MongoDB accessible at `mongodb://localhost:27017`.

### 4. Set Environment Variables (Optional)

If you're using a custom MongoDB URI or need to configure other environment variables, create a `.env` file in the project root:

```bash
touch .env
```

Add the MongoDB URI or other configurations to `.env`:

```plaintext
MONGO_URI=mongodb://localhost:27017/
```

Alternatively, you can set environment variables directly in your terminal:

```bash
export MONGO_URI=mongodb://localhost:27017/
```

### 5. Run the Pipeline

Once MongoDB is running and dependencies are installed, you can run the pipeline:

```bash
python src/pipeline.py
```

The pipeline performs the following tasks:
1. Retrieves clinical trial data from the clinicaltrials.gov API.
2. Maps and transforms the data to match the specified JSON schema.
3. Inserts the transformed data into MongoDB.
4. Extracts diseases from the `eligibilityCriteria` field and updates MongoDB records.

---

## Verify Data in MongoDB

To confirm that data was successfully added to MongoDB:

1. Open a MongoDB shell:

   ```bash
   mongo
   ```

2. Switch to the `clinical_trials_db` database:

   ```javascript
   use clinical_trials_db
   ```

3. View the inserted documents:

   ```javascript
   db.clinical_trials.find().pretty()
   ```

You should see the clinical trial data, including any extracted diseases.

---

## Future Improvements

1. **Add NLP-Based Disease Extraction**: Replace keyword-based disease extraction with an NLP model for more accuracy.
2. **Parallelize Data Processing**: For large datasets, introduce parallel processing to speed up data retrieval and transformation.
3. **Add Data Source Flexibility**: Allow the pipeline to ingest data from multiple clinical trial registries.
4. **Add Docker Compose Support**: Include a `docker-compose.yml` file to automate the setup of MongoDB and the pipeline in separate containers.

---

This `README.md` should guide you through the setup, execution, and verification steps required to run this project successfully. If you have any issues, please consult MongoDB and Python documentation or open an issue in the repository.
