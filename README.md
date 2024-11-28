# Project Directory Structure

This document outlines the directory structure of the project, which includes both backend and frontend components.


---

## **Details**

### **Backend**
- **Folder:** `backend/`
  - **`app.py`**: Contains the Flask application code that serves the API.
  - **`isolation_forest_model.pkl`**: Pre-trained Isolation Forest model for predictions.
  - **`scaler.pkl`**: StandardScaler object used for feature scaling.
  - **`requirements.txt`**: List of dependencies required for the backend.
  - **`README.md`**: Instructions for setting up and running the backend.

### **Frontend**
- **Folder:** `frontend/`
  - **`index.html`**: Main HTML file for the web interface.
  - **`style.css`**: (Optional) CSS file for styling the interface.
  - **`script.js`**: JavaScript logic for handling user interactions and API calls.
  - **`README.md`**: Instructions for setting up and using the frontend.

### **Root**
- **`README.md`**: Overview of the entire project, including setup and usage instructions for both frontend and backend.

---

## **Project Setup**
Follow the instructions in the respective `README.md` files within the `backend/` and `frontend/` folders for detailed setup and usage.



# Deployment Guide

## Deploying Your Project on Render and Vercel

This guide will walk you through the process of deploying both the backend and frontend of your project using Render and Vercel. 

### Prerequisites
- Ensure you have a GitHub account and your project is pushed to a GitHub repository.
- Create accounts on [Render](https://render.com/) and [Vercel](https://vercel.com/) if you haven't already.

---

## Deploying the Backend on Render

### Step 1: Connect to Render
1. Go to [Render](https://render.com/) and log in or create a new account.
2. Click on **New** and select **Web Service**.

### Step 2: Set Up the Service
1. **Connect your GitHub Account**: If you haven't linked your GitHub account, you will be prompted to do so.
2. **Select Your Repository**: Choose the repository containing your backend code.
3. **Configure the Service**:
   - **Name**: Enter a name for your backend service.
   - **Environment**: Choose `Python`.
   - **Root Directory**: Choose `./backend`.

   - **Build Command**: Use the command to install dependencies, usually `pip install -r requirements.txt`.

   - **Start Command**: Specify how to start your application (e.g., `python app.py` or `gunicorn app:app` depending on your setup).
   - **Region**: Select the region closest to your user base.

### Step 3: Environment Variables
- Add any necessary environment variables that your application requires (e.g., database URLs, API keys) in the **Environment Variables** section.

### Step 4: Deploy
1. Click **Create Web Service** to start the deployment process.
2. Render will automatically build and deploy your backend application.

---

## Deploying the Frontend on Vercel

### Step 1: Connect to Vercel
1. Go to [Vercel](https://vercel.com/) and log in or create a new account.
2. Click on **New Project**.

### Step 2: Import Your GitHub Repository
1. Vercel will prompt you to import a project from GitHub. Select the repository containing your frontend code.
2. If prompted, authorize Vercel to access your GitHub account.

### Step 3: Configure Project Settings
1. **Framework Preset**: Choose the appropriate framework for your frontend (e.g., React, Next.js, etc.).
2. **Root Directory**: If your frontend is in a subdirectory, specify that directory.
    - **Root Directory**: Choose `./frontend`.

3. **Environment Variables**: Add any environment variables if needed for your frontend.

### Step 4: Deploy
1. Click **Deploy** to start the deployment process.
2. Vercel will automatically build and deploy your frontend application.

---

## Accessing Your Deployed Applications
- Once deployed, you will receive unique URLs for both your backend and frontend applications. You can access them directly from the Render and Vercel dashboards.

---

## Post-Deployment Configuration

After deploying your applications, you'll need to update the API endpoint in your frontend code to ensure it points to the correct backend service URL.

### Update the API Endpoint

1. Open the `script.js` file located in the `frontend/` folder.
2. Replace API endpoint  'http://127.0.0.1:5000/predict' this with actual URL of your deployed backend service on Render. 








